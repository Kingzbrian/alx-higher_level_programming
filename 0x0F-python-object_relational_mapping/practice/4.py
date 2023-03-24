#!/usr/bin/python3
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], host='localhost', port=3306)

    cur = db.cursor()
    res = """SELECT cities.id, cities.name, states.name from states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id asc"""
    cur.execute(res)
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
