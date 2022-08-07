#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost', port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities INNER JOIN \
            states ON cities.state_id = states.id WHERE \
            states.name=%s ORDER BY cities.id;", (argv[4],))

    rows = cursor.fetchall()

    value = []
    for row in rows:
        value.append(row[0])

    print(", ".join(value))

    cursor.close()
    db.close()
