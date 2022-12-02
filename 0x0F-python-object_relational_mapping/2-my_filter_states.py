#!/usr/bin/env python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ != "__main__":
    return
mydb = MySQLdb.connect(host="localhost", user=argv[1],
                       db=argv[3], port=3306, passwd=argv[2])
cur = mydb.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY states.id".format(argv[4]))  # noqa
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
mydb.close()
