#!/usr/bin/env python

from threading import Thread, Lock
import random
import time

stdout_lock = Lock()

def doit(num):  # <1>
    time.sleep(random.randint(1, 3))
    with stdout_lock:
        print("Hello from thread {}".format(num))


for i in range(10):
    t = Thread(target=doit, args=(i,))  # <2>
    t.start()  # <3>

print("Done.")  # <4>
