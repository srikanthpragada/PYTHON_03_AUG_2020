# List employees from EMPLOYEES table

import sqlite3

con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
cur = con.cursor()
cur.execute("select * from employees order by salary desc")

for emp in cur.fetchall():
    print(f"{emp[0]:5} {emp[1]:30} {emp[2]:10} {emp[3]:8}")

con.close()
