---
title: owncloud
type: docs
---

> **WARNING**: This Ansible role is currently in beta state. Use it at your own risk. 

Ansible role to setup an ownCloud server. Currently, only a single ownCloud server is supported. Support for clustered mode is planned but not included right now.

* [Default Variables](#default-variables)
  * [owncloud_admin_password](#owncloud-admin-password)
  * [owncloud_admin_username](#owncloud-admin-username)
  * [owncloud_allow_user_to_change_display_name](#owncloud-allow-user-to-change-display-name)
  * [owncloud_apcu_enabled](#owncloud-apcu-enabled)
  * [owncloud_app_documents_enabled](#owncloud-app-documents-enabled)
  * [owncloud_app_documents_provider](#owncloud-app-documents-provider)
  * [owncloud_app_group](#owncloud-app-group)
  * [owncloud_apps](#owncloud-apps)
  * [owncloud_apps_config](#owncloud-apps-config)
  * [owncloud_autosetup](#owncloud-autosetup)
  * [owncloud_config_extra](#owncloud-config-extra)
  * [owncloud_config_path](#owncloud-config-path)
  * [owncloud_cors_allowed_domains](#owncloud-cors-allowed-domains)
  * [owncloud_cron_backend](#owncloud-cron-backend)
  * [owncloud_cron_jobs](#owncloud-cron-jobs)
  * [owncloud_csrf_enabled](#owncloud-csrf-enabled)
  * [owncloud_data_path](#owncloud-data-path)
  * [owncloud_db_host](#owncloud-db-host)
  * [owncloud_db_name](#owncloud-db-name)
  * [owncloud_db_password](#owncloud-db-password)
  * [owncloud_db_tableprefix](#owncloud-db-tableprefix)
  * [owncloud_db_type](#owncloud-db-type)
  * [owncloud_db_user](#owncloud-db-user)
  * [owncloud_default_app](#owncloud-default-app)
  * [owncloud_deploy_path](#owncloud-deploy-path)
  * [owncloud_download_url](#owncloud-download-url)
  * [owncloud_enable_avatars](#owncloud-enable-avatars)
  * [owncloud_encryption_enabled](#owncloud-encryption-enabled)
  * [owncloud_encryption_force_encrypt_all](#owncloud-encryption-force-encrypt-all)
  * [owncloud_federation_allow_incoming_server2server_share](#owncloud-federation-allow-incoming-server2server-share)
  * [owncloud_federation_allow_outgoing_server2server_share](#owncloud-federation-allow-outgoing-server2server-share)
  * [owncloud_federation_auto_accept_trusted](#owncloud-federation-auto-accept-trusted)
  * [owncloud_federation_auto_add_servers](#owncloud-federation-auto-add-servers)
  * [owncloud_fqdn](#owncloud-fqdn)
  * [owncloud_install_from_filesystem](#owncloud-install-from-filesystem)
  * [owncloud_integrity_ignore_missing_app_signature](#owncloud-integrity-ignore-missing-app-signature)
  * [owncloud_knowledgebase_enabled](#owncloud-knowledgebase-enabled)
  * [owncloud_log_cron](#owncloud-log-cron)
  * [owncloud_log_dateformat](#owncloud-log-dateformat)
  * [owncloud_log_file](#owncloud-log-file)
  * [owncloud_log_level](#owncloud-log-level)
  * [owncloud_log_rotate_size](#owncloud-log-rotate-size)
  * [owncloud_log_timezone](#owncloud-log-timezone)
  * [owncloud_log_type](#owncloud-log-type)
  * [owncloud_login_alternatives](#owncloud-login-alternatives)
  * [owncloud_mail_smtp_auth_enabled](#owncloud-mail-smtp-auth-enabled)
  * [owncloud_medial_search_accounts_enabled](#owncloud-medial-search-accounts-enabled)
  * [owncloud_occ_executable](#owncloud-occ-executable)
  * [owncloud_packages_extra](#owncloud-packages-extra)
  * [owncloud_password_force_change_on_first_login](#owncloud-password-force-change-on-first-login)
  * [owncloud_redis_enabled](#owncloud-redis-enabled)
  * [owncloud_redis_host](#owncloud-redis-host)
  * [owncloud_redis_port](#owncloud-redis-port)
  * [owncloud_release_channel](#owncloud-release-channel)
  * [owncloud_remember_login_cookie_lifetime](#owncloud-remember-login-cookie-lifetime)
  * [owncloud_search_min_length](#owncloud-search-min-length)
  * [owncloud_session_keepalive_enabled](#owncloud-session-keepalive-enabled)
  * [owncloud_session_lifetime](#owncloud-session-lifetime)
  * [owncloud_share_api_allow_group_sharing](#owncloud-share-api-allow-group-sharing)
  * [owncloud_share_api_allow_links](#owncloud-share-api-allow-links)
  * [owncloud_share_api_allow_mail_notification](#owncloud-share-api-allow-mail-notification)
  * [owncloud_share_api_allow_public_notification](#owncloud-share-api-allow-public-notification)
  * [owncloud_share_api_allow_public_upload](#owncloud-share-api-allow-public-upload)
  * [owncloud_share_api_allow_resharing](#owncloud-share-api-allow-resharing)
  * [owncloud_share_api_allow_share_dialog_user_enumeration](#owncloud-share-api-allow-share-dialog-user-enumeration)
  * [owncloud_share_api_allow_social_share](#owncloud-share-api-allow-social-share)
  * [owncloud_share_api_auto_accept_share](#owncloud-share-api-auto-accept-share)
  * [owncloud_share_api_default_expire_date](#owncloud-share-api-default-expire-date)
  * [owncloud_share_api_enabled](#owncloud-share-api-enabled)
  * [owncloud_share_api_enforce_expire_date](#owncloud-share-api-enforce-expire-date)
  * [owncloud_share_api_enforce_password_links_read_only](#owncloud-share-api-enforce-password-links-read-only)
  * [owncloud_share_api_enforce_password_links_read_write](#owncloud-share-api-enforce-password-links-read-write)
  * [owncloud_share_api_enforce_password_links_write_only](#owncloud-share-api-enforce-password-links-write-only)
  * [owncloud_share_api_expire_after_n_days](#owncloud-share-api-expire-after-n-days)
  * [owncloud_share_api_only_share_with_group_members](#owncloud-share-api-only-share-with-group-members)
  * [owncloud_share_api_only_share_with_membership_groups](#owncloud-share-api-only-share-with-membership-groups)
  * [owncloud_share_api_share_dialog_user_enumeration_group_members](#owncloud-share-api-share-dialog-user-enumeration-group-members)
  * [owncloud_show_server_hostname](#owncloud-show-server-hostname)
  * [owncloud_skeleton_path](#owncloud-skeleton-path)
  * [owncloud_src_path](#owncloud-src-path)
  * [owncloud_syslog_log_format](#owncloud-syslog-log-format)
  * [owncloud_syslog_tag](#owncloud-syslog-tag)
  * [owncloud_system_group](#owncloud-system-group)
  * [owncloud_system_user](#owncloud-system-user)
  * [owncloud_system_user_comment](#owncloud-system-user-comment)
  * [owncloud_system_user_home](#owncloud-system-user-home)
  * [owncloud_system_user_shell](#owncloud-system-user-shell)
  * [owncloud_token_auth_enforced](#owncloud-token-auth-enforced)
  * [owncloud_trusted_domains](#owncloud-trusted-domains)
  * [owncloud_upgrade_3party_app_disable](#owncloud-upgrade-3party-app-disable)
  * [owncloud_upgrade_migration_test](#owncloud-upgrade-migration-test)
  * [owncloud_version](#owncloud-version)
  * [owncloud_version_hide](#owncloud-version-hide)
  * [owncloud_web_default_language](#owncloud-web-default-language)
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
