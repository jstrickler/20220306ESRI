#!/usr/bin/env python
from datetime import date
import sqlite3


with sqlite3.connect("../DATA/presidents.db") as s3conn:  # <1>

    sql_insert = """
    insert into presidents 
    (termnum, lastname, firstname, birthdate, deathdate, birthplace, birthstate, termstart, termend, party)
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
    """


    new_row_data = [47, 'Ramirez', 'Mary', date(1968, 9, 22), None,
                    'Topeka', 'Kansas', date(2024, 1, 20), None, 'Independent']

    cursor = s3conn.cursor()

    try:
        cursor.execute(sql_insert, new_row_data)
    except (sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.DataError) as err:
        print(err)
        s3conn.rollback()
    else:
        s3conn.commit()

    cursor.close()
