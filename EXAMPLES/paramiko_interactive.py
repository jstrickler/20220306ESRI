#!/usr/bin/env python
import paramiko
# bc is an interactive calculator that comes with Unix-like systems (Linux, Mac, etc.)

with paramiko.SSHClient() as ssh:  # <.>
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # <.>

    ssh.connect('localhost', username='python', password='l0lz')  # <.>

    stdin, stdout, stderr = ssh.exec_command('bc')  # <.>

    stdin.write("17 + 25\n")  # <.>
    result = stdout.readline()  # <.>
    print("Result is:", result)

    stdin.write("scale = 3\n")  # <.>
    stdin.write("738.3/191.9\n")
    result = stdout.readline()
    print("Result is:", result)

    stdin.write("quit\n")  # <.>
    stdin = None   # <.>



