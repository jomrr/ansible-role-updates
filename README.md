# ansible-role-updates

![GitHub](https://img.shields.io/github/license/jam82/ansible-role-updates) ![GitHub last commit](https://img.shields.io/github/last-commit/jam82/ansible-role-updates) ![GitHub issues](https://img.shields.io/github/issues-raw/jam82/ansible-role-updates) ![Travis (.com) branch](https://img.shields.io/travis/com/jam82/ansible-role-updates/main?label=travis) [![Molecule](https://github.com/jam82/ansible-role-updates/actions/workflows/molecule.yml/badge.svg)](https://github.com/jam82/ansible-role-updates/actions/workflows/molecule.yml)

**Ansible role for configuring automatic updates.**

The defaults of this role will install all available updates daily.

On Debian-based systems it additionally will:

- reboot at 04:00 a.m., if required and no users are logged in
- autoremove unused kernel packages
- autofix broken packages
- Send mail to root, only on error

## Supported Platforms

| OS Family | Distribution  | Latest | Supported Version(s) | Comment |
|-----------|---------------|--------|----------------------|---------|
| Debian    | Debian        | :heavy_check_mark: | 10, 11 | |
|           | Ubuntu        | :heavy_check_mark: | 18.04, 20.04 | |
|           | Raspbian      | :heavy_check_mark: | 10, 11 | |
| RedHat    | CentOS        | :heavy_check_mark: | 7, 8 | |
|           | Fedora        | :heavy_check_mark: | 33, 34, Rawhide | |

## Requirements

Ansible 2.9 or higher.

## Variables

Variables and defaults for this role:

### defaults/main/main.yml

Variables affecting multiple package managers

```yaml
---
# role: ansible-role-updates
# file: defaults/main/main.yml

# The role is disabled by default, so you do not get in trouble.
# Checked in tasks/main.yml which includes tasks.yml if enabled.
updates_role_enabled: false

# download upgradeable packages
updates_download: true

# apply downloaded upgrades
updates_apply: true

# blacklisted packages, that will not be upgraded (regexp possible)
updates_blacklist: []

# random sleep in minutes for dnf and yum
updates_random_sleep: 120

# emitters for dnf/yum, can be empty, 'None', 'stdio', 'email'
updates_emit_via: 'None'

# update email from
updates_email_from: 'root'

# update email to
updates_email_to:
  - 'root'

# update email host
updates_email_host: 'localhost'

# system name in emails for dnf/yum, defaults to hostname
updates_system_name: ''
```

### defaults/main/apt.yml

Variables affecting **unattended-upgrades** only

```yaml
---
# role: ansible-role-updates
# file: defaults/main/apt.yml

# issue apt-get autoremove every n days
updates_autoclean_interval: 1

# update package lists every n days
updates_packages_lists: 1

# allowed_origins for debian based distros
updates_origins:
  - "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}"
  - "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}-backports"
  - "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}-updates"
  - "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}-security"
  - "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }},l={{ ansible_distribution }}-Security"

# update ubuntu dev release
updates_dev_release: false

# autofix interrupted updates, should be true to continue getting updates
updates_autofix: true

# split the upgrade into the smallest possible chunks so that they can be interrupted with SIGTERM
updates_minimal_steps: true

# install updates on shutdown only
updates_install_on_shutdown: false

# only send mail on error
updates_mail_only_on_error: true

# remove unused kernels
updates_remove_kernels: true

# remove unused dependencies
updates_remove_dependencies: false

# automatic reboot
updates_reboot: true

updates_reboot_with_users: false

# time for automatic reboot
updates_reboot_time: "04:00"

# bandwith limit in KB/s
updates_dl_limit: 0

# log to syslog
updates_syslog: true

# syslog facility to use
updates_syslog_facility: 'daemon'

# run on ac power only
updates_on_ac_only: true

# only run on unmetered connections
updates_unmetered: true
```

### defaults/main/dnf.yml

Variables affecting **dnf-automatic** only

```yaml
---
# role: ansible-role-updates
# file: defaults/main/dnf.yml

# update_cmd for dnf, default installs als updates
updates_dnf_update_cmd: 'default'

# override dnf.conf settings
# e.g. - { debuglevel: 1 }
updates_dnf_base:
  - { debuglevel: 1 }

# format of command as python format string in str.format(), e.g. "cat"
updates_dnf_command_format: ''

# contents of stdin to pass to the command, e.g. "{body}"
updates_dnf_stdin_format: ''

# format of mail command as python format string in str.format(),
# e.g. "mail -s {subject} -r {email_from} {email_to}"
updates_dnf_email_command_format: ''

# contents of stdin to pass to the email command, e.g. "{body}"
updates_dnf_email_stdin_format: ''
```

### defaults/main/yum.yml

Variables affecting **yum-cron** only

```yaml
---
# role: ansible-role-updates
# file: defaults/main/yum.yml

# update_cmd for yum, default installs als updates
updates_yum_update_cmd: 'default'

# override yum.conf settings, e.g. debuglevel
# e.g. - { debuglevel: -2 }
updates_yum_base: []

# Whether a message should be emitted when updates are available,
# were downloaded, or applied.
updates_yum_update_message: false

# output width of the emitted message, default 80
updates_yum_message_output_width: 80
```

## Dependencies

None.

## Example Playbook

```yaml
---
# role: ansible-role-updates
# file: site.yml

- hosts: all
  become: true
  gather_facts: true
  vars:
    updates_enabled: true
  roles:
    - role: ansible-role-updates
```

## License and Author

- Author:: [jam82](https://github.com/jam82/)
- Copyright:: 2020, [jam82](https://github.com/jam82/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jam82/ansible-role-updates/blob/master/LICENSE) file in repository.

## References

- [Debian Wiki](https://wiki.debian.org/UnattendedUpgrades)
- [Fedora Wiki](https://fedoraproject.org/wiki/AutoUpdates)
- [Q's Tutorials](https://www.stqu.de/joomla/index.php/raspberry-pi/90-pi-automatische-updates-unattended-upgrades)
- [Redhat](https://access.redhat.com/solutions/10185)
- [Ubuntu Help](https://help.ubuntu.com/lts/serverguide/automatic-updates.html)
