#!/usr/bin/env python
import threading  # <1>
import random
import time

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()

MAX_SLEEP_TIME = 3
WORD_LIST = []  # <2>
WORD_LIST_LOCK = threading.Lock()  # <3>
STDOUT_LOCK = threading.Lock()  # <3>

class SimpleThread(threading.Thread):
    def __init__(self, num, word):  # <4>
        super().__init__()  # <5>
        self._word = word
        self._num = num

    def run(self):  # <6>
        time.sleep(random.randint(1, MAX_SLEEP_TIME))
        with STDOUT_LOCK:  # <7>
            print("Hello from thread {} ({})".format(self._num, self._word))

        with WORD_LIST_LOCK:  # <7>
            WORD_LIST.append(self._word.upper())

all_threads = []  # <8>
for i, random_word in enumerate(WORDS, 1):
    t = SimpleThread(i, random_word)  # <9>
    all_threads.append(t)  # <10>
    t.start()  # <11>

print("All threads launched...")

for t in all_threads:
    t.join()  # <12>

print(WORD_LIST)
