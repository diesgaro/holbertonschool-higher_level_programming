#!/usr/bin/python3
"""
Python script that get and prints the cities with his state
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
    query = "SELECT city.id, city.name, state.name" \
            " FROM cities AS city" \
            " INNER JOIN states AS state ON city.state_id = state.id" \
            " ORDER BY city.id ASC;"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
