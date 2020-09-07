# List employees from EMPLOYEES table

import sqlite3

con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
cur = con.cursor()
cur.execute("select sum(salary), count(*) from employees")
row = cur.fetchone()
print(f"Total Salary     : {row[0]}")
print(f"No. of Employees : {row[1]}")
con.close()
