#!/usr/bin/env python

import urllib.request

u = urllib.request.urlopen("https://www.python.org")

print(u.info())  # <1>
print()

print(u.read(500).decode())   # <2>
