#!/usr/bin/python3

"""
A script that lists all cities from the database hbtn_0e_4_usa
while Showing the state name of each city
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                 FROM cities INNER JOIN states
                 ON cities.state_id = states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
