#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], host='localhost', port=3306)
    cur = db.cursor()
    res = """SELECT cities.name FROM states INNER JOIN cities on states.id = cities.state_id WHERE states.name=%s ORDER BY cities.id"""
    cur.execute(res, (argv[4],))
    cities = cur.fetchall()

    ccities = []
    for city in cities:
        ccities.append(city[0])
    print (", ".join(ccities))
