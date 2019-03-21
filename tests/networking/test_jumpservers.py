import pytest


def test_ips(ssh):
    try:
        stdin, stdout, stderr = ssh.exec_command(f'ping -c 3 {dest}')

    assert exit_status == estatus
