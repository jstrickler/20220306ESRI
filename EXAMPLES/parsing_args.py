#!/usr/bin/env python
import re
import fileinput
import argparse

arg_parser = argparse.ArgumentParser(description="Emulate grep with python")  # <3>

arg_parser.add_argument(
    '-i',
    dest='ignore_case', action='store_true',
    help='ignore case'
)  # <4>

arg_parser.add_argument('-n', dest="show_name", action="store_true", help="display file name")

arg_parser.add_argument(
    'pattern', help='Pattern to find (required)'
)  # <5>

arg_parser.add_argument(
    'filenames', nargs='*',
    help='filename(s) (if no files specified, read STDIN)'
)  # <6>

args = arg_parser.parse_args()  # <7>

print('-' * 40)
print(args)
print('-' * 40)

regex = re.compile(args.pattern, re.I if args.ignore_case else 0)  # <8>

for line in fileinput.input(args.filenames):  # <11>
    if regex.search(line):
        if args.show_name:
            print(fileinput.filename(), end=": ")
        print(line.rstrip())
