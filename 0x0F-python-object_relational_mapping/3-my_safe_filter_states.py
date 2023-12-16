#!/usr/bin/python3
"""
A script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
It should be safe from MySQL injections!
"""


import MySQLdb
import sys


if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
