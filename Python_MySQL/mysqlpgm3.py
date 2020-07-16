import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminar",
    auth_plugin='mysql_native_password'
)


cursor=db.cursor()


sql="""Insert into EMPLOYEE_ONE(
        FIRST_NAME,
        LAST_NAME,
        AGE,
        SEX,
        INCOME ) values('NAVMI','V',27,'F','2500')"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)

db.close()