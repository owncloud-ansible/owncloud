#!/usr/bin/python
# Standards: 0.1
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Robert Kaussow <mail@geeklabor.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ['preview'], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: oc_config
short_description: Manages ownCloud system and app config
description:
  - "Manage ownCloud system and app config. To use this module, the following keys are required: C(attribute)
  and C(value)."
version_added: "2.9"
options:
  name:
    description:
      - The namespace to work on. Can be 'system' or '<app_name>'.
    default: 'system'
  attribute:
    description:
      - Name of the config attribute.
  value:
    description:
      - The new value of the config attribute.
  type:
    description:
      - The Value type (string, integer, double, boolean, json).
      - Would be ignored if name is not 'system'.
  state:
    description:
      - The state of module. 'absent' will delete specified config attribute.
    choices: [ absent, present ]
    default: present
  update_only:
    description:
      - Only updates the value, if it is not set before, it is not being added.
    type: bool
    default: 'no'
  chdir:
    description:
      - cd into this directory before running the command
    version_added: "2.9"
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
'''  # noqa

EXAMPLES = '''
# Set password policy.
- oc_config:
    name: password_policy
    attribute: minLength
    value: 12

# Set system config attribute.
- oc_config:
    name: system
    attribute: logtimezone
    value: "Europe/Berlin"
'''

RETURN = '''
tbd
'''

import os
import tempfile
import hashlib

from ansible.module_utils.basic import AnsibleModule  # noqa
from ansible.module_utils._text import to_native  # noqa
from ansible.module_utils.six import PY3  # noqa


def _get_state_map(name):
    scope = 'config:app:'

    if name == 'system':
        scope = 'config:system:'

    resultmap = dict(
        present=[scope + 'set'],
        absent=[scope + 'delete'],
    )

    return resultmap


def _get_hash(value):
    value = value.encode('utf-8')
    return hashlib.md5(value).hexdigest()


def _get_current_config(occ, module, chdir, name, attribute):
    err = ''
    out = ''

    if name == 'system':
        cmd = [occ] + ['config:system:get', attribute]
    else:
        cmd = [occ] + ['config:app:get', name, attribute]

    rc, out_occ, err_occ = module.run_command(cmd, cwd=chdir)
    out += out_occ
    err += err_occ

    if rc == 1:
        out_occ = ""
        pass
    elif rc != 0:
        _fail(module, cmd, out, err)

    module.log(msg=out_occ)

    return out


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
            module.fail_json(
                msg='Unable to find any of %s to use. occ'
                ' needs to be installed.' % ', '.join(candidate_occ_basenames)
            )

    return occ


def _fail(module, cmd, out, err):
    msg = ''
    if out:
        msg += "stdout: %s" % (out,)
    if err:
        msg += "\n:stderr: %s" % (err,)
    module.fail_json(cmd=cmd, msg=msg)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['present', 'absent']),
            name=dict(type='str'),
            update_only=dict(type='bool', default=False),
            attribute=dict(type='str'),
            value=dict(type='str'),
            type=dict(
                type='str',
                choices=['string', 'integer', 'double', 'boolean', 'json'],
                default='string'
            ),
            chdir=dict(type='path'),
            executable=dict(type='path'),
        ),
        required_together=[['name', 'attribute', 'value']],
        supports_check_mode=False,
    )

    state = module.params['state']
    name = module.params['name']
    update_only = module.params['update_only']
    attribute = module.params['attribute']
    value = module.params['value']
    vtype = module.params['type']
    chdir = module.params['chdir']

    state_map = _get_state_map(name)

    if chdir is None:
        # this is done to avoid permissions issues with privilege escalation
        chdir = tempfile.gettempdir()

    err = ''
    out = ''

    occ = _get_occ(module, module.params['executable'])
    cmd = [occ] + state_map[state]
    before_value = _get_current_config(occ, module, chdir, name, attribute)

    if name:
        if not name == 'system':
            cmd.append(name)
    else:
        module.exit_json(
            changed=False,
            warnings=["No valid name found."],
        )

    cmd.append(attribute)

    if state == 'present':
        cmd.extend(['--value', value])
        if name == 'system':
            cmd.extend(['--type', vtype])

        if update_only:
            cmd.append('--update-only')

    rc, out_enable, err_enable = module.run_command(cmd, cwd=chdir)
    if rc != 0:
        _fail(module, cmd, out_enable, err_enable)

    after_value = _get_current_config(occ, module, chdir, name, attribute)

    changed = not _get_hash(before_value) == _get_hash(after_value)

    module.exit_json(changed=changed, cmd=cmd, name=name, state=state, stdout=out, stderr=err)


if __name__ == '__main__':
    main()
