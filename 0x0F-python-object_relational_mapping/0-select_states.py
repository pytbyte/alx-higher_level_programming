#!/usr/bin/python3

"""_0-select_states.py
    lists all states from database hbtn_0e_0usa_
    this program uses MySQLdb
"""
import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="root", db="hbtn_0e_0_usa",
                       charset="utf8")
cur = conn.cursor()

cur.execute("select * from states ORDER BY id Asc;")
results = cur.fetchall()

for i in results:
    print(i)
cur.close()
conn.close()
