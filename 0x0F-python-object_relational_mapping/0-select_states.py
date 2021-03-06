#!/usr/bin/python3
"""
Python script that get and show all rows in database table
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
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
