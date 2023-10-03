#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states INNER JOIN cities ON states.id = cities.state_id WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    cities = cur.fetchall()

    print(",".join([city[0] for city in cities]))

    cur.close()
    db.close()
