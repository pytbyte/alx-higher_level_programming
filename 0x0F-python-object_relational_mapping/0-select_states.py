#!/usr/bin/python3
"""0-select_states
python database manipulation program
1.checks args and assigns them accordingly or print error messageand exit.
2.initiates database connection from args values supplied
3.runs db query and prints results or error message
4.closes the database connection
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password,
                               db=database_name, charset="utf8")
        cur = conn.cursor()

        query = "SELECT * FROM states ORDER BY id ASC;"
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cur.close()
        conn.close()
