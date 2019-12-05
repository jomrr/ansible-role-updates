# ansible-role-updates ![GitHub](https://img.shields.io/github/license/jam82/ansible-role-updates) [![Build Status](https://travis-ci.org/jam82/ansible-role-updates.svg?branch=master)](https://travis-ci.org/jam82/ansible-role-updates)

Ansible role for configuring automatic updates.

The defaults of this role will install all available updates daily.

On Debian-based systems it additionally will:

* reboot at 04:00 a.m., if required and no users are logged in
* autoremove unused kernel packages
* autofix broken packages
* Send mail to root, only on error

## Supported Platforms

* CentOS 7, 8
* Debian 9, 10
* Oracle 7, 8
* Raspbian 9, 10
* Ubuntu 16.04, 18.04

## Requirements

Ansible 2.7 or higher is recommended.

## Variables

Variables and defaults for this role:

### Variables affecting multiple package managers

| variable | default | pkg_mgr | description |
| -------- | ------- | ------- | ----------- |
| updates_enabled | False | all | Determine whether role is enabled (True) or not (False) |
| updates_apply | True | all | apply downloaded upgrades |
| updates_blacklist | [] | all | List of blacklisted packages, that will not be upgraded (regexp possible) |
| updates_download | True | all | Download upgradeable packages |
| updates_email_from | 'root' | all | FROM-Address for sending mails (dnf, yum) or recipient for apt |
| updates_email_host | 'localhost' | dnf, yum | Hostname for E-Mails |
| updates_email_to | ['root'] | dnf, yum | List of E-Mail recipients |
| updates_emit_via | 'None' | dnf, yum | Emitters, can be empty, 'None', 'stdio', 'email' |
| updates_random_sleep | 120 | dnf, yum | Random sleep in minutes for dnf and yum |
| updates_system_name | '' | dnf, yum | System name in E-Mails, defaults to hostname if empty |

### Variables affecting **unattended-upgrades** only

| variable | default | pkg_mgr | description |
| -------- | ------- | ------- | ----------- |
| updates_autoclean_interval | 1 | apt | Autoclean every n days |
| updates_autofix | True | apt | Autofix interrupted updates |
| updates_dev_release | False | apt | Update Ubuntu Development release |
| updates_dl_limit | 0 | apt | Bandwith limit in KB/s |
| updates_install_on_shutdown | False | apt | Upgrade on shutdown only |
| updates_mail_only_on_error | True | apt | Only send E-Mail on error |
| updates_minimal_steps | True | apt | Split the upgrade into the smallest possible chunks so that they can be interrupted with SIGTERM |
| updates_on_ac_only | True | apt | Run on AC power only |
| updates_origins | `- "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}"`         | apt | Origins for packages |
|                 | `- "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}-updates"` |     |                      |
|                 | `- "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }}-security"`|     |                      |
|                 | `- "origin={{ ansible_distribution }},codename={{ ansible_distribution_release }},l={{ ansible_distribution }}-Security"`| | |
| updates_packages_lists | 1 | apt | Update package lists every n days |
| updates_reboot | True | apt | Automatic reboot, if needed |
| updates_reboot_with_users | False | apt | True = reboot with users logged in, False = do not reboot with logged in users |
| updates_reboot_time | "04:00" | apt | Time for automatic reboot, 24h format |
| updates_remove_dependencies | False | apt | Autoremove unused dependencies |
| updates_remove_kernels | True | apt | Autoremove unused Kernels |
| updates_syslog | True | apt | Log to syslog |
| updates_syslog_facility | 'daemon' | apt | Syslog facility to use |
| updates_unmetered | True | apt | Only run on unmetered connections |

### Variables affecting **dnf-automatic** only

| variable | default | pkg_mgr | description |
| -------- | ------- | ------- | ----------- |
| updates_dnf_base | [] | dnf | Override dnf.conf settings, e.g. - { debuglevel: 1 } |
| updates_dnf_command_format | '' | dnf | Format of command as python format string in str.format(), e.g. "cat" |
| updates_dnf_email_command_format | '' | dnf | Format of mail command as python format string in str.format(), e.g. "mail -s {subject} -r {email_from} {email_to}" |
| updates_dnf_email_stdin_format | '' | dnf | Contents of stdin to pass to the email command, e.g. "{body}" |
| updates_dnf_stdin_format | '' | dnf | Contents of stdin to pass to the command, e.g. "{body}" |
| updates_dnf_update_cmd | 'default' | dnf | The update_cmd for dnf, 'default' installs all, 'security' only security updates |

### Variables affecting **yum-cron** only

| variable | default | pkg_mgr | description |
| -------- | ------- | ------- | ----------- |
| updates_yum_base | [] | yum | Override yum.conf settings, e.g. debuglevel, e.g. `- { debuglevel: -2 }` |
| updates_yum_message_output_width | 80 | yum | Output width of the emitted message, default 80 |
| updates_yum_update_cmd | 'default' | yum | Update_cmd for yum, 'default installs als updates' |
| updates_yum_update_message | False | yum | Whether a message should be emitted when updates are available, were downloaded, or applied |

## Dependencies

None.

## Example Playbook

```yaml
---
# role: ansible-role-updates
# file: site.yml

- hosts: updates_systems
  become: True
  vars:
    updates_enabled: True
  roles:
    - role: ansible-role-updates
```

## License and Author

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.

## References

* [Debian Wiki](https://wiki.debian.org/UnattendedUpgrades)
* [Fedora Wiki](https://fedoraproject.org/wiki/AutoUpdates)
* [Q's Tutorials](https://www.stqu.de/joomla/index.php/raspberry-pi/90-pi-automatische-updates-unattended-upgrades)
* [Redhat](https://access.redhat.com/solutions/10185)
* [Ubuntu Help](https://help.ubuntu.com/lts/serverguide/automatic-updates.html)
