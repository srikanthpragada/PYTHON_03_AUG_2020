import logging
import sqlite3

logging.basicConfig(filename=r"c:\classroom\sqlite3.log", level=logging.INFO)
try:
    con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
    logging.info("Connect to database")
    cur = con.cursor()
    id = int(input("Enter employee id :"))
    try:
        cur.execute("delete from employees where empid = ?", (id,))
        if cur.rowcount == 1:  # no. of rows updated
            print("Deleted Employee Successfully!")
            logging.info(f"Deleted employee with id : {id}")
            con.commit()
        else:
            print("Sorry! Employee id not found!")
    except Exception as ex:
        logging.error(f"Error during update : {ex}")
        print("Error while deleting employee :", ex)

except Exception as ex:
    logging.error(f"Connection Error : {ex}")
    print("Error : ", ex)

con.close()
