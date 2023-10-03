#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)

    cur = db.cursor()

    cur.execute("""SELECT id, name FROM states WHERE name LIKE %s ORDER BY id ASC""", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()

