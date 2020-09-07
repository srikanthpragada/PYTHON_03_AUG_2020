import sqlite3

con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
cur = con.cursor()
name = input("Enter  name :")
job = input("Enter job :")
salary = int(input("Enter salary :"))

try:
    cur.execute("insert into employees(name,job,salary) values(?,?,?)", (name, job, salary))
    con.commit()
    print("Added Successfully!")
except:
    print("Sorry! Could not add employee due to error!")

con.close()
