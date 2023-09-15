#!/usr/bin/python3
"""2-my_filter_states
python database manipulation program
1.checks args and assigns them accordingly or print error message and exit.
2.initiates database connection from args values supplied
3.runs db query and prints results
filtered by submited state arg  or error message
4.closes the database connection
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("./5.. <username> <password> <database_name> <state>")
        sys.exit(1)
    user, pswd, db, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=user, passwd=pswd,
                               db=db, charset="utf8")
        cur = conn.cursor()

        query = """
    SELECT DISTINCT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
        cur.execute(query, (state,))

        results = cur.fetchall()

        cities = [row[0] for row in results]
        print(", ".join(cities))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cur.close()
        conn.close()
