#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Robert Kaussow <mail@geeklabor.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: oc_app
short_description: Manages ownCloud apps
description:
     - "Manage ownCloud apps. To use this module, one of the following keys is required: C(name)
       or C(requirements)."
version_added: "2.9"
options:
  name:
    description:
      - The name of a ownCloud app to install or the url of the remote package.
      - 'market' app can't be handled by this module and therefore is not a valid value and
        the task will be skipped with a warning.
  state:
    description:
      - The state of module. 'lateste' only works while installing from the marketplace and is ignored
        if 'from_url' is set.
    choices: [ absent, latest, present, current ]
    default: present
  enabled:
    description:
      - Activate/deactivate an installed package.
    type: bool
    default: 'yes'
  from_url:
    description:
      - Install package from a custom url instead of the official marketplace.
    type: bool
    default: 'no'
  url_username:
    description:
      - The username for use in HTTP basic authentication.
      - This parameter can be used without C(url_password) for sites that allow empty passwords.
      - Since version 2.8 you can also use the C(username) alias for this option.
    type: str
    aliases: ['username']
    version_added: '1.6'
  url_password:
    description:
        - The password for use in HTTP basic authentication.
        - If the C(url_username) parameter is not specified, the C(url_password) parameter will not be used.
        - Since version 2.8 you can also use the 'password' alias for this option.
    type: str
    aliases: ['password']
    version_added: '1.6'
  force_basic_auth:
    description:
      - Force the sending of the Basic authentication header upon initial request.
      - httplib2, the library used by the uri module only sends authentication information when a webservice
        responds to an initial request with a 401 status. Since some basic auth services do not properly
        send a 401, logins will fail.
  chdir:
    description:
      - cd into this directory before running the command
  executable:
    description:
      - The explicit executable or a pathname to the executable to be used to
        run occ.
notes:
  - tbd
requirements:
  - occ
author:
  - Robert Kaussow (@xoxys)
'''

EXAMPLES = '''
# Install contacts app.
- oc_app:
    name: contacts
'''

RETURN = '''
name:
  description: name of an ownCloud apps targetted by occ
  returned: success
  type: list
  sample: 'contacts'
'''

import os
import json
import tempfile
import traceback
import shutil

import xml.etree.ElementTree as ET

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible.module_utils.urls import fetch_url, url_argument_spec
from ansible.module_utils.six.moves.urllib.parse import urlsplit


def _get_installed_apps(occ, module, chdir):
    err = ''
    out = ''

    cmd = [occ] + ['app:list', '--no-warnings', '--output', 'json']
    rc, out_occ, err_occ = module.run_command(cmd, cwd=chdir)
    out += out_occ
    err += err_occ

    json_out = json.loads(out_occ)

    if rc != 0:
        _fail(module, cmd, out, err)

    module.log(msg=out_occ)

    return list(json_out['enabled']), list(json_out['disabled'])


def _get_occ(module, executable=None):
    candidate_occ_basenames = ('occ',)
    occ = None
    if executable is not None:
        if os.path.isabs(executable):
            occ = executable
        else:
            candidate_occ_basenames = (executable,)

    if occ is None:
        for basename in candidate_occ_basenames:
            occ = module.get_bin_path(basename, False, opt_dirs=['/usr/local/bin'])
            if occ is not None:
                break
        else:
            # For-else: Means that we did not break out of the loop
            # (therefore, that occ was not found)
            module.fail_json(msg='Unable to find any of %s to use. occ'
                                 ' needs to be installed.' % ', '.join(candidate_occ_basenames))

    return occ


def url_get(module, url, timeout=10, headers=None):
    """
    Download data from the url and store in a temporary file.
    Return (tempfile, info about the request)
    """
    if module.check_mode:
        method = 'HEAD'
    else:
        method = 'GET'

    rsp, info = fetch_url(module, url, timeout=timeout, headers=headers, method=method)

    if info['status'] == 304:
        module.exit_json(url=url, changed=False, msg=info.get('msg', ''))

    # Exceptions in fetch_url may result in a status -1, the ensures a proper error to the user in all cases
    if info['status'] == -1:
        module.fail_json(msg=info['msg'], url=url)

    if info['status'] != 200 and not url.startswith('file:/') and not (url.startswith('ftp:/') and info.get('msg', '').startswith('OK')):
        module.fail_json(msg="Request failed", status_code=info['status'], response=info['msg'], url=url)

    tmp_dest = module.tmpdir

    fd, tempname = tempfile.mkstemp(dir=tmp_dest)

    f = os.fdopen(fd, 'wb')
    try:
        shutil.copyfileobj(rsp, f)
    except Exception as e:
        os.remove(tempname)
        module.fail_json(msg="failed to create temporary content file: %s" % to_native(e), exception=traceback.format_exc())
    f.close()
    rsp.close()

    fn = os.path.basename(urlsplit(url)[2])
    if fn == '':
        os.remove(tempname)
        module.fail_json(msg="Request failed. Can't detect filename in url.", url=url)
    dest = os.path.join(tmp_dest, fn)
    module.atomic_move(tempname, dest)

    return dest, info


def unarchive(module, src):
    cmd_path = module.get_bin_path('gtar', None)
    dest = module.tmpdir
    if not cmd_path:
        # Fallback to tar
        cmd_path = module.get_bin_path('tar')
    try:
        cmd = [cmd_path, '--extract', '-f', src, '--strip-components', '1']
        rc, out, err = module.run_command(cmd, cwd=dest, environ_update=dict(LANG='C', LC_ALL='C', LC_MESSAGES='C'))
        if rc != 0:
            module.fail_json(msg="failed to unpack %s to %s" % (src, dest))
    except IOError:
        module.fail_json(msg="failed to unpack %s to %s" % (src, dest))

    return dest


def _fail(module, cmd, out, err):
    msg = ''
    if out:
        msg += "stdout: %s" % (out, )
    if err:
        msg += "\n:stderr: %s" % (err, )
    module.fail_json(cmd=cmd, msg=msg)


def main():
    state_map = dict(
        present=['market:install'],
        absent=['market:uninstall'],
        latest=['market:upgrade'],
        current=[],
    )

    argument_spec = url_argument_spec()
    argument_spec.update(
        state=dict(type='str', default='present', choices=state_map.keys()),
        name=dict(type='str'),
        enabled=dict(type='bool', default=True),
        from_url=dict(type='bool', default=False),
        chdir=dict(type='path'),
        executable=dict(type='path'),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[['name']],
        mutually_exclusive=[['name']],
        supports_check_mode=False,
    )

    state = module.params['state']
    name = module.params['name']
    from_url = module.params['from_url']
    chdir = module.params['chdir']
    enable = module.params['enabled']

    url_result = dict(
        url=name,
    )

    if chdir is None:
        # this is done to avoid permissions issues with privilege escalation
        chdir = tempfile.gettempdir()

    err = ''
    out = ''

    occ = _get_occ(module, module.params['executable'])
    cmd = [occ] + state_map[state]
    enabled_apps, disabled_apps = _get_installed_apps(occ, module, chdir)

    skip_install = False
    changed_enabled = False
    changed_install = False

    tmpsrc = ''
    appinfo = ''
    if from_url:
        # download to tmpsrc
        tmpsrc, info = url_get(module, name)
        url_result['src'] = tmpsrc

        # raise an error if there is no tmpsrc file
        if not os.path.exists(tmpsrc):
            os.remove(tmpsrc)
            module.fail_json(msg="Request failed", status_code=info['status'], response=info['msg'])
        if not os.access(tmpsrc, os.R_OK):
            os.remove(tmpsrc)
            module.fail_json(msg="Source %s is not readable" % (tmpsrc))

        appinfo = os.path.join(unarchive(module, tmpsrc), 'appinfo', 'info.xml')
        xmlfile = ET.parse(appinfo)
        name = xmlfile.getroot().find('id').text

    if name and not name == 'market':
        if from_url and state == 'present':
            cmd.extend(['-l', to_native(tmpsrc)])
        else:
            package = to_native(name)
            cmd.append(package)
    else:
        module.exit_json(
            changed=False,
            warnings=["No valid name found."],
        )

    if state == 'present' and (name in enabled_apps or name in disabled_apps):
        skip_install = True

    if state == 'current':
        skip_install = True

    if not skip_install:
        rc, out_occ, err_occ = module.run_command(cmd, cwd=chdir)
        out += out_occ
        err += err_occ
        if rc == 1 and state == 'absent' and \
           ('not be uninstalled' in out_occ or 'not be uninstalled' in err_occ):
            pass  # rc is 1 when attempting to uninstall non-installed package
        elif rc != 0:
            _fail(module, cmd, out, err)

        if state == 'absent':
            changed_install = 'App uninstalled' in out_occ
        else:
            changed_install = 'App installed' in out_occ

    # enable or disable app
    if not state == 'absent':
        if enable:
            cmd = [occ] + ['app:enable', name]
        else:
            cmd = [occ] + ['app:disable', name]

        rc, out_enable, err_enable = module.run_command(cmd, cwd=chdir)
        if rc == 1 and not enable and 'No such app enabled' in out_enable:
            pass  # rc is 1 when attempting to uninstall non-installed package
        elif rc != 0:
            _fail(module, cmd, out_enable, err_enable)

        if enable:
            changed_enabled = name + ' enabled' in out_enable and name in disabled_apps
        else:
            changed_enabled = name + ' disabled' in out_enable and name in enabled_apps

    changed = changed_install or changed_enabled

    # if os.path.isfile(tmpsrc):
    #     os.remove(tmpsrc)

    # if os.path.isdir(appinfo):
    #     shutil.rmtree(appinfo)

    module.exit_json(changed=changed, cmd=cmd, name=name, state=state,
                     stdout=out, stderr=err)


if __name__ == '__main__':
    main()
