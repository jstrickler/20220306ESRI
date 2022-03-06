#!/usr/bin/env python
import psycopg2

pg_conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
pg_cursor = pg_conn.cursor()

# select first name, last name from all presidents
pg_cursor.execute('''
    select firstname, lastname from presidents order by termnum
''')

print("{} rows in result set\n".format(pg_cursor.rowcount))

for row in pg_cursor.fetchall():
    print(' '.join(row))
print()

pg_conn.close()

