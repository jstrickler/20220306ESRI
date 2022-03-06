#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # <1>


mary_in = trimmed('../DATA/mary.txt')
for trimmed_line in mary_in:  # <2>
    print(trimmed_line)


