
import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
    cur = con.cursor()
    id = int(input("Enter employee id :"))
    salary = int(input("Enter new salary :"))
    try:
      cur.execute("update employees set salary = ? where id = ?", (salary,id))
      if cur.rowcount == 1:  # no. of rows updated
        print("Updated Successfully!")
        con.commit()
      else:
        print("Sorry! Employee id not found!")
    except Exception as ex:
        print("Error while updating employee :", ex)

except Exception as ex:
    print("Error : ", ex)

con.close()
