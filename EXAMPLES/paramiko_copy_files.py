#!/usr/bin/env python
import os
import paramiko

REMOTE_DIR = 'text_files'

with paramiko.Transport(('localhost', 22)) as transport:  # <.>
    transport.connect(username='python', password='l0lz')  # <.>
    sftp = paramiko.SFTPClient.from_transport(transport)  # <.>
    for item in sftp.listdir_iter():  # <.>
        print(item)
    print('-' * 60)

    try:
        sftp.rmdir(REMOTE_DIR)
    except OSError as err:
        print(err)
    sftp.mkdir(REMOTE_DIR)

    # sftp.put(local-file)
    # sftp.put(local-file, remote-file)
    remote_path = os.path.join(REMOTE_DIR, 'betsy.txt')  # <.>
    sftp.put('../DATA/alice.txt', remote_path)  # <.>
    sftp.put('../DATA/alice.txt', 'alice.txt')
    sftp.get(remote_path, 'eileen.txt')  # <.>
    print(sftp.listdir())
    print()
    print(sftp.listdir(REMOTE_DIR))



