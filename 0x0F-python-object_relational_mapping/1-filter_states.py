#!/usr/bin/python3
"""1-filter_states
python database manipulation program
1.checks args and assigns them accordingly or print error messageand exit.
2.initiates database connection from args values supplied
3.runs db query and gets results or error message
4.filters results with regex to print city names starting with "N"
4.closes the database connection
"""
import MySQLdb
import sys
import re

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
        pattern = r'^N'

        for row in results:
            if re.match(pattern, row[1]):
                print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cur.close()
        conn.close()
