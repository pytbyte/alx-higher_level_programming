#!/usr/bin/python3
""" 
python database manipulation
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
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
