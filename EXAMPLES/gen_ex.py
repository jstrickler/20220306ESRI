#!/usr/bin/env python

# sum the squares of a list of numbers
# using list comprehension, entire list is stored in memory
s1 = sum([x * x for x in range(10)])  # <1>

# only one square is in memory at a time with generator expression
s2 = sum(x * x for x in range(10))  # <2>
print(s1, s2)
print()

with open("../DATA/mary.txt") as page:
    m = max(len(line) for line in page)  # <3>
print(m)
