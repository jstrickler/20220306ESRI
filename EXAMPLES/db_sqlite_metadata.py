#!/usr/bin/env python

"""
    Provide metadata (tables and column names) for a Sqlite3 database
"""

import sqlite3

DB_NAME = "../DATA/presidents.db"

TABLE_QUERY = '''
    select * from presidents where 1 == 2
'''


def main():
    """
        Program entry point

        PARAMS:
        database_file: name of Sqlite database file
    """
    cursor = connect_to_db(DB_NAME)
    show_metadata(cursor)


def connect_to_db(database_file):
    """
        Connect to specified Sqlite3 database

        PARAMS:
        database_file: name of Sqlite3 database file to query
    """
    with sqlite3.connect(database_file) as s3conn:
        return s3conn.cursor()

def show_metadata(cursor):
    cursor.execute(TABLE_QUERY)
    for column_info in cursor.description:
        column_name = column_info[0]
        print(f"{column_name}:", column_info[1:])




if __name__ == '__main__':
    main()
