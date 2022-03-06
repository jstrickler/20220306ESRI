#!/usr/bin/env python

import random
from multiprocessing.dummy import Pool # <1>

POOL_SIZE = 30 # <2>

with open('../DATA/words.txt') as words_in:
    WORDS = [w.strip() for w in words_in] # <3>

random.shuffle(WORDS) # <4>

def my_task(word):  # <5>
    return word.upper()

tpool = Pool(POOL_SIZE) # <6>

WORD_LIST = tpool.map(my_task, WORDS) # <7>

print(WORD_LIST[:20])  # <8>

print("Processed {} words.".format(len(WORD_LIST)))
