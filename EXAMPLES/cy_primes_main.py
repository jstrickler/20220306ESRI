#!/usr/bin/env python
import time
import py_primes
import numba_primes
import pyximport

pyximport.install() # <1>
import cy_primes # <2>

NUM_PRIMES = 100000 # <3>

for mod in numba_primes, cy_primes: # <4>

    timestamp = time.time() # <5>

    prime_list = mod.get_primes(NUM_PRIMES)  # <6>

    timestamp2 = time.time() # <7>

    elapsed = timestamp2 - timestamp  # <8>

    print(prime_list[:20], prime_list[-20:])

    print("{} took {:.3f} seconds to find {} primes".format(
        mod.__name__, elapsed, len(prime_list))) # <9>
    print()
