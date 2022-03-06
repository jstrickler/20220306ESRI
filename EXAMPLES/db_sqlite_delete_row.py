#!/usr/bin/env python
from datetime import date
import sqlite3


with sqlite3.connect("../DATA/presidents.db") as conn:  # <1>

    sql_delete = """
    delete from presidents
    where TERMNUM = 47 
    """

    cursor = conn.cursor()

    try:
        cursor.execute(sql_delete)
    except (sqlite3.DatabaseError, sqlite3.OperationalError, sqlite3.DataError) as err:
        print(err)
        conn.rollback()
    else:
        conn.commit()

    cursor.close()
