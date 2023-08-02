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

    cur.execute("SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
    cities = cur.fetchall()

    for city in cities:
        print (city)

    cur.close()
    db.close()
