#!/usr/bin/python3
"""
Python script that get and prints the cities filtered by state
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

    query = "SELECT city.name" \
            " FROM cities AS city" \
            " INNER JOIN states AS state ON city.state_id = state.id" \
            " WHERE state.name = %(state)s" \
            " ORDER BY city.id ASC;"
    cur.execute(query, {
        'state': argv[4]
    })

    rows = cur.fetchall()

    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
