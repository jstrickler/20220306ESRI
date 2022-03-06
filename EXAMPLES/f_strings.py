#!/usr/bin/env python

import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 6:

    name = "Tim"
    count = 5
    avg = 3.456
    info = 2093
    result = 38293892

    print(f"Name is [{name:<10s}]")  # <1>
    print(f"Name is [{name:>10s}]")  # <2>
    print(f"count is {count:03d} avg is {avg:.2f}")  # <3>

    print(f"info is {info} {info:d} {info:o} {info:x}")  # <4>

    print(f"${result:,d}")  # <5>

    city = 'Orlando'
    temp = 85

    print(f"It is {temp} in {city}")  # <6>

else:
    print("Sorry -- f-strings are only supported by Python 3.6+")
