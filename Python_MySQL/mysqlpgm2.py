import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminar",
    auth_plugin='mysql_native_password'
)
print(db)

cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql="""CREATE TABLE EMPLOYEE_ONE(
        FIRST_NAME CHAR(20),
        LAST_NAME CHAR(20),
        AGE INT(10),
        SEX CHAR(1),
        INCOME FLOAT(10) )"""
try:
    cursor.execute(sql)
except Exception as e:
    db.rollback()
    print(e.args)
finally:
db.close()