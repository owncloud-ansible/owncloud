---
title: owncloud
type: docs
---
Ansible role to setup an ownCloud server

* [Default Variables](#default-variables)
  * [owncloud_admin_password](#owncloud_admin_password)
  * [owncloud_admin_username](#owncloud_admin_username)
  * [owncloud_allow_user_to_change_display_name](#owncloud_allow_user_to_change_display_name)
  * [owncloud_apcu_enabled](#owncloud_apcu_enabled)
  * [owncloud_app_documents_enabled](#owncloud_app_documents_enabled)
  * [owncloud_app_documents_provider](#owncloud_app_documents_provider)
  * [owncloud_app_group](#owncloud_app_group)
  * [owncloud_apps](#owncloud_apps)
  * [owncloud_apps_config](#owncloud_apps_config)
  * [owncloud_autosetup](#owncloud_autosetup)
  * [owncloud_config_extra](#owncloud_config_extra)
  * [owncloud_config_path](#owncloud_config_path)
  * [owncloud_cors_allowed_domains](#owncloud_cors_allowed_domains)
  * [owncloud_cron_backend](#owncloud_cron_backend)
  * [owncloud_cron_jobs](#owncloud_cron_jobs)
  * [owncloud_csrf_enabled](#owncloud_csrf_enabled)
  * [owncloud_data_path](#owncloud_data_path)
  * [owncloud_db_host](#owncloud_db_host)
  * [owncloud_db_name](#owncloud_db_name)
  * [owncloud_db_password](#owncloud_db_password)
  * [owncloud_db_tableprefix](#owncloud_db_tableprefix)
  * [owncloud_db_type](#owncloud_db_type)
  * [owncloud_db_user](#owncloud_db_user)
  * [owncloud_default_app](#owncloud_default_app)
  * [owncloud_deploy_path](#owncloud_deploy_path)
  * [owncloud_download_url](#owncloud_download_url)
  * [owncloud_enable_avatars](#owncloud_enable_avatars)
  * [owncloud_encryption_enabled](#owncloud_encryption_enabled)
  * [owncloud_encryption_force_encrypt_all](#owncloud_encryption_force_encrypt_all)
  * [owncloud_federation_allow_incoming_server2server_share](#owncloud_federation_allow_incoming_server2server_share)
  * [owncloud_federation_allow_outgoing_server2server_share](#owncloud_federation_allow_outgoing_server2server_share)
  * [owncloud_federation_auto_accept_trusted](#owncloud_federation_auto_accept_trusted)
  * [owncloud_federation_auto_add_servers](#owncloud_federation_auto_add_servers)
  * [owncloud_fqdn](#owncloud_fqdn)
  * [owncloud_install_from_filesystem](#owncloud_install_from_filesystem)
  * [owncloud_integrity_ignore_missing_app_signature](#owncloud_integrity_ignore_missing_app_signature)
  * [owncloud_knowledgebase_enabled](#owncloud_knowledgebase_enabled)
  * [owncloud_log_cron](#owncloud_log_cron)
  * [owncloud_log_dateformat](#owncloud_log_dateformat)
  * [owncloud_log_file](#owncloud_log_file)
  * [owncloud_log_level](#owncloud_log_level)
  * [owncloud_log_rotate_size](#owncloud_log_rotate_size)
  * [owncloud_log_timezone](#owncloud_log_timezone)
  * [owncloud_log_type](#owncloud_log_type)
  * [owncloud_login_alternatives](#owncloud_login_alternatives)
  * [owncloud_mail_smtp_auth_enabled](#owncloud_mail_smtp_auth_enabled)
  * [owncloud_medial_search_accounts_enabled](#owncloud_medial_search_accounts_enabled)
  * [owncloud_occ_executable](#owncloud_occ_executable)
  * [owncloud_packages_extra](#owncloud_packages_extra)
  * [owncloud_password_force_change_on_first_login](#owncloud_password_force_change_on_first_login)
  * [owncloud_redis_enabled](#owncloud_redis_enabled)
  * [owncloud_redis_host](#owncloud_redis_host)
  * [owncloud_redis_port](#owncloud_redis_port)
  * [owncloud_release_channel](#owncloud_release_channel)
  * [owncloud_remember_login_cookie_lifetime](#owncloud_remember_login_cookie_lifetime)
  * [owncloud_search_min_length](#owncloud_search_min_length)
  * [owncloud_session_keepalive_enabled](#owncloud_session_keepalive_enabled)
  * [owncloud_session_lifetime](#owncloud_session_lifetime)
  * [owncloud_share_api_allow_group_sharing](#owncloud_share_api_allow_group_sharing)
  * [owncloud_share_api_allow_links](#owncloud_share_api_allow_links)
  * [owncloud_share_api_allow_mail_notification](#owncloud_share_api_allow_mail_notification)
  * [owncloud_share_api_allow_public_notification](#owncloud_share_api_allow_public_notification)
  * [owncloud_share_api_allow_public_upload](#owncloud_share_api_allow_public_upload)
  * [owncloud_share_api_allow_resharing](#owncloud_share_api_allow_resharing)
  * [owncloud_share_api_allow_share_dialog_user_enumeration](#owncloud_share_api_allow_share_dialog_user_enumeration)
  * [owncloud_share_api_allow_social_share](#owncloud_share_api_allow_social_share)
  * [owncloud_share_api_auto_accept_share](#owncloud_share_api_auto_accept_share)
  * [owncloud_share_api_default_expire_date](#owncloud_share_api_default_expire_date)
  * [owncloud_share_api_enabled](#owncloud_share_api_enabled)
  * [owncloud_share_api_enforce_expire_date](#owncloud_share_api_enforce_expire_date)
  * [owncloud_share_api_enforce_password_links_read_only](#owncloud_share_api_enforce_password_links_read_only)
  * [owncloud_share_api_enforce_password_links_read_write](#owncloud_share_api_enforce_password_links_read_write)
  * [owncloud_share_api_enforce_password_links_write_only](#owncloud_share_api_enforce_password_links_write_only)
  * [owncloud_share_api_expire_after_n_days](#owncloud_share_api_expire_after_n_days)
  * [owncloud_share_api_only_share_with_group_members](#owncloud_share_api_only_share_with_group_members)
  * [owncloud_share_api_only_share_with_membership_groups](#owncloud_share_api_only_share_with_membership_groups)
  * [owncloud_share_api_share_dialog_user_enumeration_group_members](#owncloud_share_api_share_dialog_user_enumeration_group_members)
  * [owncloud_show_server_hostname](#owncloud_show_server_hostname)
  * [owncloud_skeleton_path](#owncloud_skeleton_path)
  * [owncloud_src_path](#owncloud_src_path)
  * [owncloud_syslog_log_format](#owncloud_syslog_log_format)
  * [owncloud_syslog_tag](#owncloud_syslog_tag)
  * [owncloud_system_group](#owncloud_system_group)
  * [owncloud_system_user](#owncloud_system_user)
  * [owncloud_system_user_comment](#owncloud_system_user_comment)
  * [owncloud_system_user_home](#owncloud_system_user_home)
  * [owncloud_system_user_shell](#owncloud_system_user_shell)
  * [owncloud_token_auth_enforced](#owncloud_token_auth_enforced)
  * [owncloud_trusted_domains](#owncloud_trusted_domains)
  * [owncloud_upgrade_3party_app_disable](#owncloud_upgrade_3party_app_disable)
  * [owncloud_upgrade_migration_test](#owncloud_upgrade_migration_test)
  * [owncloud_version](#owncloud_version)
  * [owncloud_version_hide](#owncloud_version_hide)
  * [owncloud_web_default_language](#owncloud_web_default_language)
* [Dependencies](#dependencies)

---

## Default Variables

### owncloud_admin_password

#### Default value

```YAML
owncloud_admin_password: owncloud
```

### owncloud_admin_username

#### Default value

```YAML
owncloud_admin_username: admin
```

### owncloud_allow_user_to_change_display_name

#### Default value

```YAML
owncloud_allow_user_to_change_display_name: true
```

### owncloud_apcu_enabled

#### Default value

```YAML
owncloud_apcu_enabled: true
```

### owncloud_app_documents_enabled

#### Default value

```YAML
owncloud_app_documents_enabled: false
```

### owncloud_app_documents_provider

#### Default value

```YAML
owncloud_app_documents_provider: onlyoffice
```

### owncloud_app_group

#### Default value

```YAML
owncloud_app_group: '{{ owncloud_system_group }}'
```

### owncloud_apps

#### Default value

```YAML
owncloud_apps:
  - name: twofactor_totp
  - name: password_policy
```

#### Example usage

```YAML
owncloud_apps:
  - name: contacts
  - name: http://market.owncloud.local/carnet-0.16.2.tar.gz
    from_url: yes
    url_username: my_user
    url_password:my_password
    force_basic_auth: true
    state: present
```

### owncloud_apps_config

#### Default value

```YAML
owncloud_apps_config: []
```

### owncloud_autosetup

#### Default value

```YAML
owncloud_autosetup: true
```

### owncloud_config_extra

For availabe configuration options see: https://doc.owncloud.com/server/admin_manual/configuration/server/config_sample_php_parameters.html

#### Default value

```YAML
owncloud_config_extra: {}
```

### owncloud_config_path

#### Default value

```YAML
owncloud_config_path: '{{ owncloud_src_path }}/config'
```

### owncloud_cors_allowed_domains

#### Default value

```YAML
owncloud_cors_allowed_domains: []
```

### owncloud_cron_backend

Possible values are `webcron|cron|ajax`. See: https://doc.owncloud.com/server/admin_manual/configuration/server/background_jobs_configuration.htmlcron-jobs

#### Default value

```YAML
owncloud_cron_backend: cron
```

### owncloud_cron_jobs

Will be applied only if owncloud_cron_backend is 'cron'

#### Default value

```YAML
owncloud_cron_jobs:
  - name: oc cron
    job: '{{ owncloud_occ_executable }} system:cron'
    minute: '*/15'
```

### owncloud_csrf_enabled

Be careful! See https://doc.owncloud.com/server/admin_manual/configuration/server/config_sample_php_parameters.htmldisable-ownclouds-built-in-csrf-protection-mechanism

#### Default value

```YAML
owncloud_csrf_enabled: true
```

### owncloud_data_path

#### Default value

```YAML
owncloud_data_path: '{{ owncloud_src_path }}/data'
```

### owncloud_db_host

#### Default value

```YAML
owncloud_db_host: localhost
```

### owncloud_db_name

#### Default value

```YAML
owncloud_db_name: owncloud
```

### owncloud_db_password

#### Default value

```YAML
owncloud_db_password: owncloud
```

### owncloud_db_tableprefix

#### Default value

```YAML
owncloud_db_tableprefix: oc_
```

### owncloud_db_type

#### Default value

```YAML
owncloud_db_type: mysql
```

### owncloud_db_user

#### Default value

```YAML
owncloud_db_user: owncloud
```

### owncloud_default_app

#### Default value

```YAML
owncloud_default_app: files
```

### owncloud_deploy_path

#### Default value

```YAML
owncloud_deploy_path: /var/www/owncloud
```

### owncloud_download_url

You can set a custom download url especialy for the enterprise version.

#### Default value

```YAML
owncloud_download_url: https://download.owncloud.org/community/owncloud-{{ owncloud_version
  }}.tar.bz2
```

### owncloud_enable_avatars

#### Default value

```YAML
owncloud_enable_avatars: true
```

### owncloud_encryption_enabled

Only supported for ownCloud >= 10.2.1

#### Default value

```YAML
owncloud_encryption_enabled: false
```

### owncloud_encryption_force_encrypt_all

#### Default value

```YAML
owncloud_encryption_force_encrypt_all: false
```

### owncloud_federation_allow_incoming_server2server_share

#### Default value

```YAML
owncloud_federation_allow_incoming_server2server_share: true
```

### owncloud_federation_allow_outgoing_server2server_share

#### Default value

```YAML
owncloud_federation_allow_outgoing_server2server_share: true
```

### owncloud_federation_auto_accept_trusted

#### Default value

```YAML
owncloud_federation_auto_accept_trusted: false
```

### owncloud_federation_auto_add_servers

#### Default value

```YAML
owncloud_federation_auto_add_servers: false
```

### owncloud_fqdn

#### Default value

```YAML
owncloud_fqdn: owncloud.example.com
```

### owncloud_install_from_filesystem

#### Default value

```YAML
owncloud_install_from_filesystem: false
```

### owncloud_integrity_ignore_missing_app_signature

#### Default value

```YAML
owncloud_integrity_ignore_missing_app_signature: []
```

### owncloud_knowledgebase_enabled

#### Default value

```YAML
owncloud_knowledgebase_enabled: true
```

### owncloud_log_cron

#### Default value

```YAML
owncloud_log_cron: true
```

### owncloud_log_dateformat

#### Default value

```YAML
owncloud_log_dateformat: Y-m-d H:i:s.u
```

### owncloud_log_file

#### Default value

```YAML
owncloud_log_file: '{{ owncloud_data_path }}/owncloud.log'
```

### owncloud_log_level

#### Default value

```YAML
owncloud_log_level: 2
```

### owncloud_log_rotate_size

#### Default value

```YAML
owncloud_log_rotate_size: 0
```

### owncloud_log_timezone

#### Default value

```YAML
owncloud_log_timezone: Etc/UTC
```

### owncloud_log_type

#### Default value

```YAML
owncloud_log_type: owncloud
```

### owncloud_login_alternatives

Allows to specify additional login buttons on the logon screen (e.g. SSO)

#### Default value

```YAML
owncloud_login_alternatives: []
```

### owncloud_mail_smtp_auth_enabled

#### Default value

```YAML
owncloud_mail_smtp_auth_enabled: false
```

### owncloud_medial_search_accounts_enabled

#### Default value

```YAML
owncloud_medial_search_accounts_enabled: true
```

### owncloud_occ_executable

#### Default value

```YAML
owncloud_occ_executable: /usr/local/bin/occ
```

### owncloud_packages_extra

#### Default value

```YAML
owncloud_packages_extra: []
```

### owncloud_password_force_change_on_first_login

#### Default value

```YAML
owncloud_password_force_change_on_first_login: false
```

### owncloud_redis_enabled

#### Default value

```YAML
owncloud_redis_enabled: true
```

### owncloud_redis_host

#### Default value

```YAML
owncloud_redis_host: 127.0.0.1
```

### owncloud_redis_port

#### Default value

```YAML
owncloud_redis_port: 6379
```

### owncloud_release_channel

#### Default value

```YAML
owncloud_release_channel: production
```

### owncloud_remember_login_cookie_lifetime

#### Default value

```YAML
owncloud_remember_login_cookie_lifetime: 1296000
```

### owncloud_search_min_length

#### Default value

```YAML
owncloud_search_min_length: 3
```

### owncloud_session_keepalive_enabled

#### Default value

```YAML
owncloud_session_keepalive_enabled: true
```

### owncloud_session_lifetime

#### Default value

```YAML
owncloud_session_lifetime: 86400
```

### owncloud_share_api_allow_group_sharing

#### Default value

```YAML
owncloud_share_api_allow_group_sharing: false
```

### owncloud_share_api_allow_links

#### Default value

```YAML
owncloud_share_api_allow_links: true
```

### owncloud_share_api_allow_mail_notification

#### Default value

```YAML
owncloud_share_api_allow_mail_notification: true
```

### owncloud_share_api_allow_public_notification

#### Default value

```YAML
owncloud_share_api_allow_public_notification: false
```

### owncloud_share_api_allow_public_upload

#### Default value

```YAML
owncloud_share_api_allow_public_upload: true
```

### owncloud_share_api_allow_resharing

#### Default value

```YAML
owncloud_share_api_allow_resharing: false
```

### owncloud_share_api_allow_share_dialog_user_enumeration

#### Default value

```YAML
owncloud_share_api_allow_share_dialog_user_enumeration: true
```

### owncloud_share_api_allow_social_share

#### Default value

```YAML
owncloud_share_api_allow_social_share: true
```

### owncloud_share_api_auto_accept_share

#### Default value

```YAML
owncloud_share_api_auto_accept_share: false
```

### owncloud_share_api_default_expire_date

#### Default value

```YAML
owncloud_share_api_default_expire_date: true
```

### owncloud_share_api_enabled

#### Default value

```YAML
owncloud_share_api_enabled: true
```

### owncloud_share_api_enforce_expire_date

#### Default value

```YAML
owncloud_share_api_enforce_expire_date: false
```

### owncloud_share_api_enforce_password_links_read_only

#### Default value

```YAML
owncloud_share_api_enforce_password_links_read_only: false
```

### owncloud_share_api_enforce_password_links_read_write

#### Default value

```YAML
owncloud_share_api_enforce_password_links_read_write: false
```

### owncloud_share_api_enforce_password_links_write_only

#### Default value

```YAML
owncloud_share_api_enforce_password_links_write_only: false
```

### owncloud_share_api_expire_after_n_days

#### Default value

```YAML
owncloud_share_api_expire_after_n_days: 7
```

### owncloud_share_api_only_share_with_group_members

#### Default value

```YAML
owncloud_share_api_only_share_with_group_members: true
```

### owncloud_share_api_only_share_with_membership_groups

#### Default value

```YAML
owncloud_share_api_only_share_with_membership_groups: true
```

### owncloud_share_api_share_dialog_user_enumeration_group_members

#### Default value

```YAML
owncloud_share_api_share_dialog_user_enumeration_group_members: false
```

### owncloud_show_server_hostname

#### Default value

```YAML
owncloud_show_server_hostname: false
```

### owncloud_skeleton_path

#### Default value

```YAML
owncloud_skeleton_path: '{{ owncloud_deploy_path }}/core/skeleton'
```

### owncloud_src_path

#### Default value

```YAML
owncloud_src_path: /usr/local/src/{{ owncloud_system_user }}
```

### owncloud_syslog_log_format

#### Default value

```YAML
owncloud_syslog_log_format: '[%reqId%][%remoteAddr%][%user%][%app%][%method%][%url%]
  %message%'
```

### owncloud_syslog_tag

#### Default value

```YAML
owncloud_syslog_tag: ownCloud
```

### owncloud_system_group

#### Default value

```YAML
owncloud_system_group: owncloud
```

### owncloud_system_user

#### Default value

```YAML
owncloud_system_user: owncloud
```

### owncloud_system_user_comment

#### Default value

```YAML
owncloud_system_user_comment: Owncloud Application Manager
```

### owncloud_system_user_home

#### Default value

```YAML
owncloud_system_user_home: /var/local/{{ owncloud_system_user }}
```

### owncloud_system_user_shell

#### Default value

```YAML
owncloud_system_user_shell: /usr/sbin/nologin
```

### owncloud_token_auth_enforced

#### Default value

```YAML
owncloud_token_auth_enforced: false
```

### owncloud_trusted_domains

#### Default value

```YAML
owncloud_trusted_domains:
  - '{{ owncloud_fqdn }}'
```

### owncloud_upgrade_3party_app_disable

#### Default value

```YAML
owncloud_upgrade_3party_app_disable: true
```

### owncloud_upgrade_migration_test

#### Default value

```YAML
owncloud_upgrade_migration_test: true
```

### owncloud_version

#### Default value

```YAML
owncloud_version: 10.3.1
```

### owncloud_version_hide

#### Default value

```YAML
owncloud_version_hide: true
```

### owncloud_web_default_language

#### Default value

```YAML
owncloud_web_default_language: en_US
```

## Dependencies

None.
