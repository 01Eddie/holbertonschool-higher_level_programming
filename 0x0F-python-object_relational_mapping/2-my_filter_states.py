#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}'\
                    ORDER BY id ASC".format(state))

    data = cursor.fetchall()

    for state in data:
        print(state)

    cursor.close()
    db.close()
