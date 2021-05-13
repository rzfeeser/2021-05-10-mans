#!/usr/bin/env python3

import psycopg2

# update the following if your user and password for postgresql are different
# than what is shown below
user = "zach"
passw = "qwerty"

# f-string defines where to connect to
connect_str = f"dbname='testpython' user='{user}' host='localhost' password='{passw}'"

conn = psycopg2.connect(connect_str)
print("Opened database successfully")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")

cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 ) ON CONFLICT DO NOTHING")

cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 ) ON CONFLICT DO NOTHING")

cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 ) ON CONFLICT DO NOTHING")

cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 ) ON CONFLICT DO NOTHING")

conn.commit()
print("Records created successfully")

cursor = conn.cursor()

cursor.execute("SELECT * FROM COMPANY")

selects = cursor.fetchall()

#selects = cursor.execute("SELECT id, name, address, salary from COMPANY")
for row in selects:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], "\n")

print("Operation done successfully")
conn.close()

