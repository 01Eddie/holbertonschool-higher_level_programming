#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
                    WHERE SUBSTRING(name,1,1) = 'N' ORDER BY id ASC")

    data = cursor.fetchall()

    for state in data:
        print(state)

    cursor.close()
    db.close()
