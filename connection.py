# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:46:28 2021

@author: acer
"""


import mysql.connector
# Establish connection bet mysql and python
db=mysql.connection.connect(host="loaclhost", user="root", password="@pride#tech78", databse="college")

# Preapare obj for cursor method
cursor=db.cursor()

# To execute sql quiries using execute method
cursor.execute('select version()')

# fetchone to fetch  single row
data=cursor.fetchone()

print('database version is:', data)
db.close()

# Establish connection bet mysql and python
db=mysql.connection.connect(host="loaclhost", user="root", password="", databse="college")

# Preapare obj for cursor method
cursor=db.cursor()

sql='Create table student(first_name char(20) not null, age int, marks float)'
cursor.execute(sql)
db.close()


# Insert 
# Q.
import mysql.connector
# Establish connection bet mysql and python
db=mysql.connection.connect(host="loaclhost", user="root", password="", databse="college")

# Preapare obj for cursor method
cursor=db.cursor()

name=input('Enter ur name:')
age=int(input('enter ure age:'))
marks=input('Enter ure marks:')

sql="insert into student values('%s', %d, %d)"%(name, age, marks)

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print('Error', e)
    db.rollbacK()
db.close()

# Ans-
#  enter ur name: vaibhav
# enter ure age: 21
# enter ure marks: 86


# select
# Q.
# Establish connection bet mysql and python
db=mysql.connection.connect(host="loaclhost", user="root", password="", database="college")

# Preapare obj for cursor method
cursor=db.cursor()

sql="select version* from student"
cursor.execute(sql)

data=cursor.fetchall()

for d in data:
    print(d)

db.close()

# Asn-
# ("vaibhav", 21, 85)
# ("ragini", 22, 88)
# ("savita", 23, 87)
# ("Akash",21, 84)

# Q.
#fetch marks=78
db=mysql.connection.connect(host="loaclhost", user="root", password="", databse="college")
cursor=db.cursor()
sql='select marks from student where age<21'
cursor.execute(sql)

# To fetch the data
data=cursor.fetchall()
print(data)
db.close()

# Ans-
# [(85)]

# Q.
import mysql.connector

db=mysql.connection.connect(host="loaclhost", user="root", password="", databse="college")
cursor=db.cursor()
sql="select first_name marks from student where marks =85"
cursor.execute(sql)

# To fetch tha data
data=cursor.fetchall()
print(data)
db.close()

# Ans-
# [("Ragini", "vaibhav",)]


# Q. UPDATE-
import mysql.connector
db=mysql.connection.connect(host="loaclhost", user="root", password="", databse="college")

# Preapare obj for cursor method
cursor=db.cursor()
marks=int(input('Enter ur marks: '))
sql="update student set marks =%d where first_name='Ragini'"%(marks)

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print('Error ', e)
    db.rollback()
db.close()

# Ans-
# Ente ure marks: 85




# Q.DELETE-
import mysql.connector
db=mysql.connection.connect(host="loaclhost", user="root", password="", databse="college")

# Preapare obj for cursor method
cursor=db.cursor()
marks=int(input('Enter ur marks: '))

sql="delete from stduent where first_name='Ragini'"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print('Error ', e)
    db.rollback()
db.close()

# Ans-
# Ente ure marks: 75









