#!/usr/bin/env python

import paramiko

with paramiko.SSHClient() as ssh:  # <1>

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # <2>

    ssh.connect('localhost', username='python', password='l0lz')  # <3>

    stdin, stdout, stderr = ssh.exec_command('whoami')  # <4>
    print(stdout.read().decode())  # <5>
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l')  # <4>
    print(stdout.read().decode())  # <5>
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l /etc/passwd /etc/horcrux')  # <4>
    print("STDOUT:")
    print(stdout.read().decode())  # <5>
    print("STDERR:")
    print(stderr.read().decode())  # <6>
    print('-' * 60)

    del stdin  # workaround for paramiko bug!
