#!/usr/bin/python3
"""
Python script that get and show row filtered by name passing
how argument avoid sql injecction
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %(name)s ORDER BY id ASC;"
    cur.execute(query, {
        'name': argv[4]})

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
