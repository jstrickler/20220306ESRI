#!/usr/bin/env python
#

people = [ # <1>
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Brown', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]

def display_person(first_name, last_name, city, state): # <2>
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))

for person in people:  # <3>
    display_person(*person)  # <4>
