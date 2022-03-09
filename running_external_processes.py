from subprocess import run, PIPE, CalledProcessError
import shlex


cmd = "netstat -n"

cmd_words = shlex.split(cmd)

try:
    proc = run(cmd_words, stdout=PIPE)
except CalledProcessError as err:
    print(err)
    exit(1)
else:
    lines = proc.stdout.decode().splitlines()
    for line in lines:
        if "ESTAB" in line:
            print(line)

