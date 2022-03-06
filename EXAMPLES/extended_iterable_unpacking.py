#!/usr/bin/env python

values = ['a', 'b', 'c', 'd', 'e']  # <1>

x, y, *z = values  # <2>
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

x, *y, z = values  # <2>
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

*x, y, z = values  # <2>
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]

for *name, _ in people:  # <3>
    print(name)
print()
