#!/usr/bin/python3
"""
A script that takes in arguments and displays all values
that is safe from MySQL injections
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    un = argv[1]
    pw = argv[2]
    dbn = argv[3]
    state_name = argv[4]

    mydb = MySQLdb.connect(host="localhost", user=un,
                           passwd=pw, port=3306, db=dbn)
    cur = mydb.cursor()
    no_rows = cur.execute("SELEct * FROM states WHERE states.name LIKE BINARY\
                          %s ORDER BY states.id ASC", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mydb.close()
