# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:01:10 2021

@author: acer
"""


import mysql.connector
db = mysql.connector.connect(host = 'localhost',user = 'root',database = 'innerjoin',password = '@pride#tech78')
cursor = db.cursor()
cursor.execute("use innerjoin;")

print('Sir, would you like to dine-in here or should i finalise your bill?')
a = int(input('For dine-in press [1]\nFor Final bill press [2]\n'))

if a == 1:
    #Input
    name = input('Please enter Customer Name: ')
    amount = int(input('Please enter Bill Amount: '))
    #Tax
    taxes = amount*0.09
    tax = '{:.2f}'.format(taxes)
    total = amount + float(tax)*2
    def final():
        try:
            cursor.execute("insert into final_bill(Customer_Name,Initial_Amount,CGST,SGST,Total_Amount) values('%s',%d,'%s','%s',%d)"%(name,amount,tax,tax,total))
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
    def initial():
        cursor.execute("insert into bill(Name,Order_Amount) values('%s',%d);"%(name,amount))
        db.commit()
        final()
    initial()
    db.close()

else:
    search = int(input('Press [1] for searching by name\nPress [2] for searching by Order_ID\n'))
    if search == 1:
        name_id = input('Enter your name: ')
        cursor.execute("select Customer_Name,Initial_Amount,Total_Amount from final where Customer_Name = '%s'"%(name_id))
        data = cursor.fetchall()
        if len(data) == 1:
            print('Customer Name is %s'%(data[0][0]))
            print('Your bill amount was %s'%(data[0][1]))
            print('Your Total Amount including taxes was',data[0][2])    
        else:
            print('Sir there are many records here, can you guess your order date?')
            date = input('Please enter your order_date in format(YYYY-MM-DD): ')
            cursor.execute('select Customer_Name,Initial_Amount,Total_Amount from final where DATE(order_date) LIKE "%s";'%('%'+ date + '%'))
            date = cursor.fetchall()
            print('Customer Name is %s'%(date[0][0]))
            print('Your initial bill amount was %s'%(date[0][1]))
            print('Your Total Amount including taxes was',date[0][2])
            
    else:
        order = int(input('Please Enter Order_ID: '))
        cursor.execute('select Customer_Name,Initial_Amount,Total_Amount from final where Order_ID = %d;'%(order))
        data = cursor.fetchall()
        print('Customer Name is %s'%(data[0][0]))
        print('Your bill amount was %s'%(data[0][1]))
        print('Your Total Amount including taxes was',data[0][2])
        
        
        
        