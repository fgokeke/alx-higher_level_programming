#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit(1)

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
