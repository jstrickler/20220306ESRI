#!/usr/bin/env python
import sys
import random
from multiprocessing import Manager, Lock, Process, Queue, freeze_support
from queue import Empty
import time

NUM_ITEMS = 25000  # <1>
POOL_SIZE = 100


class RandomWord():  # <2>
    def __init__(self):
        with open('../DATA/words.txt') as words_in:
            self._words = [word.rstrip('\n\r') for word in words_in]
        self._num_words = len(self._words)

    def __call__(self):  # <3>
        return self._words[random.randrange(0, self._num_words)]


class Worker(Process):  # <4>

    def __init__(self, name, queue, lock, result):  # <5>
        Process.__init__(self)
        self.queue = queue
        self.result = result
        self.lock = lock
        self.name = name

    def run(self):  # <6>
        while True:
            try:
                word = self.queue.get(block=False)  # <7>
                word = word.upper()  # <8>
                with self.lock:
                    self.result.append(word)  # <9>

            except Empty:  # <10>
                break


if __name__ == '__main__':
    if sys.platform == 'win32':
        freeze_support()

    word_queue = Queue()  # <11>

    manager = Manager()  # <12>
    shared_result = manager.list()  # <13>
    result_lock = Lock()  # <14>

    random_word = RandomWord()  # <15>
    for i in range(NUM_ITEMS):
        w = random_word()
        word_queue.put(w)  # <16>

    start_time = time.ctime()

    pool = []  # <17>
    for i in range(POOL_SIZE):  # <18>
        worker_name = "Worker {:03d}".format(i)
        w = Worker(worker_name, word_queue, result_lock, shared_result)  # <19>
        #
        w.start()  # <20>
        pool.append(w)  # <21>

    for t in pool:
        t.join()  # <22>

    end_time = time.ctime()

    print((shared_result[-50:]))  # <23>
    print(len(shared_result))
    print(start_time)
    print(end_time)
