#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/presidents.db") as conn:  # <1>

    cursor = conn.cursor()  # <2>

    # select first name, last name from all presidents
    cursor.execute('''
        select *
        from presidents
    ''')  # <3>

    print("Sqlite3 does not provide a row count\n")  # <4>

    for row in cursor.fetchall():  # <5>
        print(row)
#        print(' '.join(row))  # <6>

