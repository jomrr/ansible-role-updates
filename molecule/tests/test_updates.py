import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_automatic_updates(host):
    os = host.system_info.distribution
    debian_prefix = 'DEBIAN_FRONTEND=noninteractive; '
    debian_cmd = debian_prefix + 'sudo unattended-upgrade --dry-run'
    rh_path = '/usr/bin/dnf-automatic'
    rh_args = ' --no-installupdates --no-downloadupdates'
    rh_cmd = rh_path + rh_args

    if os == 'centos':
        assert host.file("/etc/os-release").contains("CentOS")
        if host.file(rh_path).exists:
            cmd = host.run(rh_cmd)
            assert cmd.rc == 0

    elif os == 'debian':
        assert host.file("/etc/os-release").contains("Debian")
        cmd = host.run(debian_cmd)
        assert cmd.rc == 0

    elif os == 'oracle':
        assert host.file("/etc/os-release").contains("Oracle")
        if host.file(rh_path).exists:
            cmd = host.run(rh_cmd)
            assert cmd.rc == 0

    elif os == 'ubuntu':
        assert host.file("/etc/os-release").contains("Ubuntu")
        cmd = host.run(debian_cmd)
        assert cmd.rc == 0
