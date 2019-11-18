import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_owncloud_running_services(host):
    assert host.service("apache2").is_running
    assert host.service("mariadb").is_running
    assert host.service("redis-server").is_running


def test_owncloud_network(host):
    assert host.socket("tcp://127.0.0.1:80").is_listening


def test_owncloud_web(host):
    code = int(host.run("curl -s -w '%{http_code}' http://localhost/index.php/login -o /dev/null").stdout)
    body = host.run("curl -sX GET http://localhost/index.php/login").stdout

    assert code == 200
    assert "ownCloud" in body


def test_owncloud_cli(host):
    status = host.run("sudo -u www-data occ status | tr -d ' '").stdout

    assert "versionstring:10.3.1" in status
    assert "installed:true" in status 
