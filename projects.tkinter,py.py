# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:36:27 2021

@author: acer
"""



#     P r o j e  c  t  -  1



from tkinter import *
from tkinter import *
top=tk.Tk()

top.title('_Rating_Of_Equipment')
top.configure(bg='red')
top.geometry('')




l1=Label(top, text='Motor_Name :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l1.grid(row=0, column=0)

e1=Entry(top,bg='white', fg='black')
e1.grid(row=0, column=1)



l2=Label(top, text='Voltage :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l2.grid(row=1, column=0)

e2=Entry(top,bg='white', fg='black')
e2.grid(row=1, column=1)



l3=Label(top, text='Current :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l3.grid(row=2, column=0)

e3=Entry(top,bg='white', fg='black')
e3.grid(row=2, column=1)



l4=Label(top, text='Power :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l4.grid(row=3, column=0)

e4=Entry(top,bg='white', fg='black')
e4.grid(row=3, column=1)



l5=Label(top, text='Resistance :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l5.grid(row=4, column=0)

e5=Entry(top,bg='white', fg='black')
e5.grid(row=4, column=1)

def show():
    tkinter.messagebox.showinfo("save", "securely save the data")
b=tkinter.Button(top, text="Save", font=('Times new Roman', 15, 'bold'), bg='gray', fg='black', command=show)
b.grid(row=7, column=0, padx=5, pady=5)



Motor_Name=tk.StringVar()
Voltage=tk.IntVar()
Current=tk.IntVar()
Power=tk.IntVar()
Resistance=tk.IntVar()


def clear():
        Motor_Name.set('')
        Voltage.set('')
        Current.set('')
        Power.set('')
        Resistance.set('')
        tkinter.messagebox.showinfo("Clear", "securely clear the data")
b1=tkinter.Button(top, text="Clear", font=('Times new Roman', 15, 'bold'), bg='gray', fg='black', command=clear)
b1.grid(row=7, column=1, padx=15, pady=15)



def Quick():
    ask=tk.messagebox.askyesno('Warning','Do you really want to Quick')
    if ask>0:
        top.destroy()
b2=tkinter.Button(top, text="Quick", font=('Times new Roman', 15, 'bold'), bg='gray', fg='black', command=Quick)
b2.grid(row=7, column=2, padx=5, pady=5)

top.mainloop()



from tkinter import *
import tkinter
top=Tk()
top.configure(bg='cyan')

b=tkinter.Canvas(width=500, height=500, bg='red')
b.create_rectangle(25,25,475,475, fill='black')
b.create_oval(50,50,450,450, fill='yellow')
b.create_oval(100,100,400,400, fill='green')
b.create_oval(150,150,350,350, fill='silver')
b.create_oval(200,200,300,300, fill='orange')
b.grid(padx=25, pady=25)

top.mainloop()



from tkinter import * 
window=Tk()
window.configure(bg='gray')
b=tkinter.Canvas(width=450, height=250, bg='red')
b.create_arc(0,0,150,150, fill='yellow', start=0, extent=150)
b.grid(padx=435, pady=45)

window.mainloop()






     #     P r o j e  c  t  -  2
from tkinter import *
top=Tk()
top.configure(bg='red')

l=Label(top, text='Student Registartion Panel', font=('Times new Roman', 20, 'bold'),width=20, bg='red', fg='black')
l.grid(row=0, column=1)

l1=Label(top, text='Enter Name :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l1.grid(row=1, column=0)

e1=Entry(top, bg='white', fg='black')
e1.grid(row=1, column=1)

l2=Label(top, text='Enter Age :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l2.grid(row=2, column=0)

e2=Entry(top, bg='white', fg='black')
e2.grid(row=2, column=1)


l3=Label(top, text='Select Gender :', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l3.grid(row=3, column=0)


var=IntVar()
c1=Radiobutton(top, text='Male', variable=var, value=1)
c1.grid(row=3, column=1)
c2=Radiobutton(top, text='Female', variable=var, value=2)
c2.grid(row=3, column=2)

l4=Label(top, text='Select Room', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l4.grid(row=4, column=0)

lst=[1,2,3,4,5]
c=IntVar()
droplst=OptionMenu(top, c, *lst)
droplst.config(width=15)
c.set('Select Room Type')
droplst.grid(row=4, column=1)

l5=Label(top, text='Select Course', font=('Times new Roman', 15, 'bold'), bg='red', fg='black')
l5.grid(row=5, column=0)


var1=IntVar()
c2=Checkbutton(top, text='Java', variable=var1)
c2.grid(row=5, column=1)
c3=Checkbutton(top, text='Python', variable=var1)
c3.grid(row=5, column=2)

import tkinter
def show():
    tkinter.messagebox.showinfo('Submit', 'Submit your form. ')
b=tkinter.Button(top, text='Submit', font=('Times new Roman', 15, 'bold'), bg='gray', fg='black', command=show)
b.grid(row=7, column=1, padx=15, pady=20)

def display():
    tkinter.messagebox.showinfo('Exit', "Exit your page. ")
b1=tkinter.Button(top, text='Exit', command=display, font=('Times new Roman', 15, 'bold'), bg='gray', fg='black')
b1.grid(row=8, column=1, padx=15, pady=15)


top.mainloop()








#     P r o j e  c  t  -  3



from tkinter import *
top=Tk()
top.configure(bg='gray')
top.geometry('500x500')

l=Label(top, text='Identity Card', font=('Times new Roman', 20, 'bold'), bg='pink', fg='black', width=25)
l.grid(row=0, column=2, padx=15, pady=15)


l1=Label(top, text='Student_Name :', font=('Times new Roman', 15, 'bold'), bg='gray', fg='black')
l1.grid(row=1, column=0)

e1=Entry(top, bg='green', fg='white', width=25)
e1.grid(row=1, column=1)



l2=Label(top, text='Date Of Birth  :', font=('Times new Roman', 15, 'bold'), bg='gray', fg='black')
l2.grid(row=2, column=0)

e2=Entry(top, bg='green', fg='white', width=25)
e2.grid(row=2, column=1)


l3=Label(top, text='Roll No  :', font=('Times new Roman', 15, 'bold'), bg='gray', fg='black')
l3.grid(row=3, column=0)


lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
c=IntVar()
droplst=OptionMenu(top, c, *lst)
droplst.configure(width=20, bg='cyan', fg='black')
c.set('Select')
droplst.grid(row=3, column=1)



l4=Label(top, text='Gender  :', font=('Times new Roman', 15, 'bold'), bg='gray', fg='black')
l4.grid(row=4, column=0)

var=IntVar()
c=Checkbutton(top, text='Male', variable=var, bg='orange')
c.grid(row=4, column=1)
c1=Checkbutton(top, text='Female', variable=var, bg='orange')
c1.grid(row=4, column=2)




l5=Label(top, text='Langauge  :', font=('Times new Roman', 15, 'bold'), bg='gray', fg='black')
l5.grid(row=5, column=0)

var1=IntVar()
v=Radiobutton(top, text='English', variable=var1, bg='pink')
v.grid(row=5, column=1)
v1=Radiobutton(top, text='Hindi', variable=var1, bg='pink')
v1.grid(row=5, column=2)


import tkinter
def show():
    ask=tk.messagebox.askyesno('Warning','Do you really want to Set')
    if ask>0:
        top.destroy()
a=tkinter.Button(top, text='Set', command=show,  font=('Times new Roman', 10, 'bold'), bg='red', fg='black', width=18)
a.grid(row=6, column=1, padx=15, pady=15)
    
def display():
    ask=tk.messagebox.askyesno('Warning', 'Do you really want to reset')
    if ask>=0:
        top.destroy()
a1=tkinter.Button(top, text="Reset",command=display, font=('Times new Roman', 10, 'bold'), bg='red', fg='black', width=18)
a1.grid(row=6, column=2, padx=10, pady=10)

top.mainloop()



  #     P r o j e  c  t  -  4
from tkinter import *
top=Tk()
top.title('Cortana')
top.configure(bg='black')

t=tkinter.Canvas(bg='black')
t.create_oval(170,70,220,140, fill='cyan')
t.grid(row=0, column=2, padx=10, pady=10)

l=Label(top, text="Sign in to Cortana", font=('Times new Roman', 25, 'bold'), bg='black', fg='white', width=20)
l.grid(row=1, column=2, padx=15, pady=15)

def show():
    tkinter.messagebox.showinfo('Sign in', 'Sign is successful!')
b=tkinter.Button(top, text="Sign in", comman=show, bg='white',fg='black', font=('Times new Roman', 15, 'bold'), width=18, height=1)
b.grid(row=4, column=2, padx=12, pady=12)


l1=Label(top, text='For the best experience use your work or scholl/university account.', font=('Times new Roman', 18, 'bold'), bg='black', fg='white')
l1.grid(row=5, column=2)

top.mainloop()





#     P r o j e  c  t  -  5

from tkinter import *
top=Tk()
import tkinter
top.configure(bg='cyan')

l=Label(top, text='Student Name :', font=('Times new Roman', 15, 'bold'), bg='cyan', fg='black', width=12)
l.grid(row=0, column=0, pady=15)

e=Entry(top, bg='green', fg='white', font=('Times new Roman', 15, 'bold'))
e.grid(row=0, column=1)

l1=Label(top, text='Gender :', font=('Times new Roman', 15, 'bold'), bg='cyan', fg='black', width=12)
l1.grid(row=1, column=0)

var=IntVar()
c=Checkbutton(top, text='Male', variable=var,bg='orange', fg='black')
c.grid(row=1, column=1)

c1=Radiobutton(top, text='Female',variable=var, bg='orange',fg='black')
c1.grid(row=1, column=2)

l2=Label(top, text='Course Type  :', font=('times new Roman', 10, 'bold'), bg='cyan', fg='black', width=12)
l2.grid(row=2, column=0)

lst=['Electrical Engineering', 'Mechanical Engineering', 'Information Technology ', 'Computer Engineering', 'Civil Engineering', 'Electronice & Electrical Engineering', 'Chemical Engineering']
c=StringVar()
droplst=OptionMenu(top, c, *lst)
droplst.configure(width=20, bg='pink', fg='black')
c.set('Select')
droplst.grid(row=2, column=1)

top.mainloop()






#     P r o j e  c  t  -  6

from tkinter import *
import tkinter
top=Tk()
top.configure(bg='white')
top.title('Login Page')

l=Label(top, text='Sign Up', font=("Times new Roman",45, 'bold'), bg='white', fg='black', width=22)
l.grid(row=0, column=1)


l=Label(top, text='Its free & always will be.', font=("Times new Roman",24), bg='white', fg='red')
l.grid(row=1, column=1, pady=25, padx=35)


l=Label(top, text='First Name : ', bg='white', fg='black', font=('Purisa', 15, 'bold'))
l.grid(row=2, column=0, padx=5, pady=5)
e=Entry(top, text='First Name', font=('Times new Roman', 15, 'bold'), bg='silver',fg='red')
e.grid(row=2, column=1)



l=Label(top, text='Last Name : ', fg='black', bg='white', font=('Purisa', 15, 'bold'))
l.grid(row=3, column=0)
e=Entry(top, text='Last Name', font=('Times new Roman', 15, 'bold'), bg='silver',fg='red')
e.grid(row=3, column=1)


l=Label(top,  text='Mobile No / E-mail : ', fg='black', bg='white', font=('Purisa', 15, 'bold'))
l.grid(row=4, column=0)
e=Entry(top, font=('Times new Roman', 15, 'bold'), bg='silver',fg='red', width=30 )
e.grid(row=4, column=1)

 
l=Label(top,  text='New Password :', fg='black', bg='white', font=('Purisa', 15, 'bold'))
l.grid(row=5, column=0)
e=Entry(top,  font=('Times new Roman', 15, 'bold'), fg='red',bg='silver' , width=30)
e.grid(row=5, column=1)

top.mainloop()




#     P r o j e  c  t  -  7
from tkinter import *
top=Tk()
import tkinter

l=Label(top, text='Enter Gmail :', font=('Tmes new Roman', 10, 'bold'), bg='white', fg='black')
l.grid(row=0, column=0)

e=Entry(top, bg='white', fg='black')
e.grid(row=0, column=1)


l2=Label(top, text='Enter Password :', font=('Tmes new Roman', 10, 'bold'), bg='white', fg='black')
l2.grid(row=1, column=0)

e2=Entry(top, bg='white', fg='black')
e2.grid(row=1, column=1)

def show():
    ask=tkinter.messagebox.showinfo('Warning', 'Do you really want to submit.')
b=tkinter.Button(top, text='Submit', comman=show, font=('Times new Roman', 10,'bold'), bg='white', fg='black')
b.grid(row=2, column=0)


def display():
    ask=tkinter.messagebox.showinfo('Warning', 'Do you really want to Register.')
b=tkinter.Button(top, text='Register', comman=display, font=('Times new Roman', 10,'bold'), bg='white', fg='black')
b.grid(row=2, column=1)


top.mainloop()





#     P r o j e  c  t  -  8
from tkinter import *
top=Tk()
import tkinter
top.configure(bg='cyan')
top.title('Google')

l=Label(top, text='Username :', font=('Tmes new Roman', 12, 'bold'), bg='cyan', fg='black')
l.grid(row=0, column=0, pady=15)

e=Entry(top, bg='white', fg='black')
e.grid(row=0, column=1, pady=15)


l2=Label(top, text= 'Password :', font=('Tmes new Roman', 12, 'bold'), bg='cyan', fg='black')
l2.grid(row=1, column=0)

e2=Entry(top, bg='white', fg='black')
e2.grid(row=1, column=1)

def show():
    ask=tkinter.messagebox.showinfo('Warning', 'Do you really want to submit.')
b=tkinter.Button(top, text='Submit', comman=show, font=('Times new Roman', 10,'bold'), bg='gray', fg='black')
b.grid(row=2, column=1, pady=20)

top.mainloop()


#     P r o j e  c  t  -  9
from tkinter import *
top=Tk()
import tkinter
top.configure(bg='silver')

l=Label(top, text='I  N  D  E  X', font=('Times new Roman', 30, 'bold'), bg='silver', fg='black', width=25)
l.grid(row=0, column=3, pady=25)


l1=Label(top, text='Sr. No', font=('Times new Roman', 17, 'bold'), bg='silver', fg='black', width=20)
l1.grid(row=2, column=0, padx=5)

l1=Label(top, text=' R e m a r k s ', font=('Times new Roman', 17, 'bold'), bg='silver', fg='black', width=20)
l1.grid(row=2, column=70, padx=5)



l2=Label(top, text='T i t l e', font=('Times new Roman', 17, 'bold'), bg='silver', fg='black', width=20)
l2.grid(row=2, column=30, padx=5, pady=10, columnspan=24)


top.mainloop()




#     P r o j e  c  t  -  10

from tkinter import *
import tkinter as tk
top=Tk()
top.configure(bg='gray')
top.geometry('500x500')

mf=tk.Frame(top, bg='red') 
mf.place(x=470, y=155,width=600, height=550)


l=tk.Label(mf, text='PRN No:', font=('Times new Roman',15, 'bold'), bg='red', fg='black', width=12)
l.grid(row=0, column=0, pady=17)

e=tk.Entry(mf, bg='white', fg='black', width=22)
e.grid(row=0, column=1, pady=15, padx=35)


l=tk.Label(mf, text='College Name:', font=('Times new Roman',15, 'bold'), bg='red', fg='black', width=12)
l.grid(row=1, column=0, pady=15, padx=25)

e=tk.Entry(mf, bg='white', fg='black', width=22)
e.grid(row=1, column=1, padx=35)



l=tk.Label(mf, text='Course Year:', font=('Times new Roman',15, 'bold'), bg='red', fg='black', width=10)
l.grid(row=2, column=0, pady=15, padx=25)


lst=['FE', "SE", 'TE', "BE"]
c=IntVar()
c.set('Select')
droplst=OptionMenu(mf, c, *lst)
droplst.configure(width=20, bg='pink')
droplst.grid(row=2, column=1)



l=tk.Label(mf, text='Course Types:', font=('Times new Roman',15, 'bold'), bg='red', fg='black', width=10)
l.grid(row=3, column=0, pady=15, padx=25)

lst1=['Chemical Engineering', 'Electrical Engineering', 'Electronics Engineering', 'Mechanical Enigineering', 'Civil Engineering', 'Computer Engineering', 'Information Technology Engineering']
c=IntVar()
c.set('Select Specilasation')
droplst=OptionMenu(mf, c, *lst1)
droplst.configure(width=20, bg='cyan')
droplst.grid(row=3, column=1)



l=tk.Label(mf, text='Shift Time:', font=('Times new Roman',15, 'bold'), bg='red', fg='black', width=10)
l.grid(row=4, column=0, pady=15, padx=25)



lst2=['7:30 to 12:30', '10:30 to 3:30', '12:45 to 5:30']
c=IntVar()
c.set('Select')
droplst=OptionMenu(mf, c, *lst2)
droplst.configure(width=20, bg='yellow')
droplst.grid(row=4, column=1)


l=tk.Label(mf, text='Hostel:', font=('Times new Roman',15, 'bold'), bg='red', fg='black', width=10)
l.grid(row=5, column=0, pady=15, padx=25)

var=StringVar()
r=Radiobutton(mf, text='Yes', font=('Times new Roman', 10, 'bold'), bg='green',fg='white', width=15)
r.grid(row=5, column=1)

r=Radiobutton(mf, text='No', font=('Times new Roman', 10, 'bold'), bg='blue',fg='white', width=15)
r.grid(row=5, column=2)

top.mainloop()



#     P r o j e  c  t  -  11

import tkinter as tk
    
top=tk.Tk()
top.title('Google')
top.configure(bg='black')
top.geometry('600x500')

t_f=tk.Frame(top, bg='cyan')
t_f.place(x=100, y=100,width=400, height=200)


la=tk.Label(top, text='Sign Up', font=('Times new Roman', 24, 'bold'), fg='red', bg='black', width=28)
la.grid(row=0, column=4, pady=15, padx=25)

l=tk.Label(t_f,text='Username :', font=('Times new Roman', 10, 'bold'), bg='red', fg='black', width=12)
l.grid(row=1,column=0,pady=15, padx=25)

e=tk.Entry(t_f,bg='white', fg='gray')
e.grid(row=1, column=1)


l1=tk.Label(t_f, text='Password :', font=('Times new Roman', 10, 'bold'), bg='red', fg='black', width=12)
l1.grid(row=2,column=0,pady=20, padx=25)


e1=tk.Entry(t_f,bg='white', fg='gray')
e1.grid(row=2, column=1)

def show():
    ask=tk.messagebox.askyesno('Warning', 'Do you really want to Login.')
b=tk.Button(t_f, text='Login', command=show, font=('purisa', 15, 'bold'), bg='silver', fg='black', width=8)
b.grid(row=3, column=2,pady=30)
top.mainloop()






#     P r o j e  c  t  -  12

import tkinter as tk
from tkinter import *
top=tk.Tk()
top.configure(bg='gray')
top.title('Adhar Card')
top.geometry('500x500')

mf=tk.Frame(top, bg='silver')
mf.place(x=150, y=30, width=500, height=700)




l1=tk.Label(mf, text='Name :', font=('purisa', 12, 'bold'), bg='silver', fg='black')
l1.grid(row=0, column=0, pady=15)

e1=tk.Entry(mf, bg='white', fg='red')
e1.grid(row=0, column=1)

l2=tk.Label(mf, text='Date of Birth :', font=('purisa', 12, 'bold'), bg='silver', fg='black')
l2.grid(row=1, column=0)

e2=tk.Entry(mf, bg='white', fg='red')
e2.grid(row=1, column=1)



l3=tk.Label(mf, text='Gender :', font=('purisa', 12, 'bold'), bg='silver', fg='black', width=9)
l3.grid(row=2, column=0, pady=15)



var=IntVar()
c=Checkbutton(mf, text='Male', variable=var, bg='orange')
c.grid(row=2, column=1)
c1=Checkbutton(mf, text='Female', variable=var, bg='orange')
c1.grid(row=2, column=2)

l4=tk.Label(mf, text='Address line1 :', font=('purisa', 15, 'bold'), bg='silver', fg='black')
l4.grid(row=3, column=0)

e4=tk.Entry(mf, bg='white', fg='red', width=25)
e4.grid(row=3, column=1, padx=25)


l5=tk.Label(mf, text='Permanent Address :', font=('purisa', 15, 'bold'), bg='silver', fg='black')
l5.grid(row=4, column=0)

e5=tk.Entry(mf, bg='white', fg='red', width=25)
e5.grid(row=4, column=1, padx=25)


l6=tk.Label(mf, text='Phon_no :', font=('purisa', 15, 'bold'), bg='silver', fg='black')
l6.grid(row=5, column=0)

e6=tk.Entry(mf, bg='white', fg='red', width=25)
e6.grid(row=5, column=1, padx=25)


l6=tk.Label(mf, text='Select Adhar number:',  font=('purisa', 15, 'bold'), bg='silver', fg='black')
l6.grid(row=6, column=0)

lst=[1516165154,4548151555515,5755215888788,887851255888,88110364877654,8796316977979]
c=IntVar()
c.set('Select Adhar Number')
droplst=OptionMenu(mf, c, *lst)
droplst.configure(width=20)
droplst.grid(row=6, column=1)


l1=tk.Label(mf, text='Photo', font=('purisa', 12, 'bold'), bg='pink', fg='black', width=11)
l1.place(x=200, y=270, width=85, height=100)




l1=tk.Label(mf, text='Bar Code',  font=('purisa', 12, 'bold'), bg='gray', fg='black', width=11)
l1.place(x=180, y=380, width=200, height=180)

top.mainloop()











#     P r o j e  c  t  -  13

import tkinter
import tkinter as tk
from tkinter import *
top=Tk()
top.configure(bg='gray')
top.geometry('500x500')

mf=tk.Frame(top, bg='maroon')
mf.place(x=225, y=40, width=268, height=550)


l=tk.Label(mf, text='Name',bg='yellow', fg='black', width=22)
l.grid(row=0, column=0, padx=50, pady=18)

e=tk.Entry(mf, bg='yellow', fg='black', width=25)
e.grid(row=1, column=0, padx=50)



l=tk.Label(mf, text='+91 Phon_n',bg='pink', fg='black', width=22)
l.grid(row=2, column=0, padx=50, pady=18)

e=tk.Entry(mf, bg='pink', fg='black', width=25)
e.grid(row=3, column=0, padx=50)


l=tk.Label(mf, text='Code',bg='orange', fg='black', width=22)
l.grid(row=4, column=0, padx=50, pady=18)

e=tk.Entry(mf, bg='orange', fg='black', width=25)
e.grid(row=5, column=0, padx=50)


l=tk.Label(mf, text='Password',bg='red', fg='black', width=22)
l.grid(row=6, column=0, padx=50, pady=18)

e=tk.Entry(mf, bg='red', fg='black', width=25)
e.grid(row=7, column=0, padx=50)



l=tk.Label(mf, text='Set of Password',bg='gray', fg='black', width=22)
l.grid(row=8, column=0, padx=50, pady=18)

e=tk.Entry(mf, bg='gray', fg='black', width=25)
e.grid(row=9, column=0, padx=50)



l=tk.Label(mf, text='Invite',bg='cyan', fg='black', width=22)
l.grid(row=10, column=0, padx=50, pady=18)

e=tk.Entry(mf, bg='cyan', fg='black', width=25)
e.grid(row=11, column=0, padx=50)


def show():
    tkinter.messagebox.showinfo('eClerx', ' Your Already Registered.')
b=tk.Button(mf, text='Registered', command=show, bg='pink', fg='maroon')
b.grid(row=12, column=0, pady=9)


def display():
    tkinter.messagebox.showinfo('eClerx', 'Already have a account.')
b=tk.Button(mf, text='Login', command=display, bg='pink', fg='maroon')
b.grid(row=13, column=0, pady=7)

top.mainloop()





#     P r o j e  c  t  -  14

import tkinter as tk
from tkinter import *
import tkinter
top=Tk()


top.configure(bg='black')
top.geometry('500x500')

mf=tk.Frame(top, bg='red')
mf.place(x=225, y=40, width=480, height=350)


l=tk.Label(mf, text='Project_Name:', font=('Times new Roman', 10, 'bold'), bg='cyan', fg='black', width=22)
l.grid(row=0, column=0, padx=40, pady=25)

tuples=('Electrical Engineering Projet','Robotics with microcontroller', 'microprocessor','Ic base Project', 'Electrical circuit', 'Electrical Motor',
      'Information Technology Engineering','Matplot based on Project', 'Numpy based on Project', 'Data Anlaysis', 'Data structure', 'Training, Testing & Spliting')
c=IntVar()
droptuples=OptionMenu(mf, c, *tuples)
droptuples.configure(width=20,bg='green', fg='white')
droptuples.grid(row=0, column=1, padx=12)
c.set('Select Name')



l=tk.Label(mf, text='Project_Leader:', font=('Times new Roman', 10, 'bold'), bg='pink', fg='black', width=22)
l.grid(row=1, column=0, padx=20, pady=10)

e=tk.Entry(mf, bg='white', fg='black')
e.grid(row=1, column=1)



l=tk.Label(mf, text='Project_Member1:', font=('Times new Roman', 10, 'bold'), bg='yellow', fg='black', width=22)
l.grid(row=2, column=0, padx=20, pady=5)

e=tk.Entry(mf, bg='white', fg='black')
e.grid(row=2, column=1)



l=tk.Label(mf, text='Project_Member2:', font=('Times new Roman', 10, 'bold'), bg='yellow', fg='black', width=22)
l.grid(row=3, column=0, padx=20, pady=5)

e=tk.Entry(mf, bg='white', fg='black')
e.grid(row=3, column=1)


l=tk.Label(mf, text='Project_Member3:', font=('Times new Roman', 10, 'bold'), bg='yellow', fg='black', width=22)
l.grid(row=4, column=0, padx=20,pady=5)


e=tk.Entry(mf, bg='white', fg='black')
e.grid(row=4, column=1)


l=tk.Label(mf, text='Project_Member4:', font=('Times new Roman', 10, 'bold'), bg='yellow', fg='black', width=22)
l.grid(row=5, column=0, padx=20, pady=5)


e=tk.Entry(mf, bg='white', fg='black')
e.grid(row=5, column=1)


def show():
    tkinter.messagebox.showinfo('COETJ', 'Send you feeddback response.')
b=tkinter.Button(mf, text='Save', command=show, bg='orange', fg='black', width=15, anchor=E, relief=GROOVE) # relief =SUNKEN, GROOVE, RAISED, RIDGE.
b.grid(row=6, column=1,pady=40, padx=35)    
                                                                                 #  anchor= E , W , CENTER.
    
top.mainloop()





#     P r o j e  c  t  -  15

from tkinter import *
import tkinter as tk
top=tk.Tk()
top.configure(bg='cyan')
top.geometry('500x500')

mf=tk.Frame(top, bg='black')
mf.place(x=400, y=40, width=750, height=530)

lmf=tk.Frame(mf, bg='red')
lmf.place(x=15, y=25, width=350, height=315)

rmf=tk.Frame(mf, bg='red')
rmf.place(x=385, y=25, width=350, height=315)




#Create variable :
sid=tk.StringVar()
f_name=tk.StringVar()
l_name=tk.StringVar()
clss=tk.StringVar()
stream=tk.StringVar()
email=tk.StringVar()
python=tk.IntVar()
sql=tk.IntVar()
ml=tk.IntVar()
total=tk.IntVar()
grade=tk.IntVar()
percentage=tk.IntVar()
    

l=tk.Label(lmf,text='Id :', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=0, column=0, pady=15, padx=20)

e=tk.Entry(lmf, bg='white', fg='black')
e.grid(row=0, column=1)


l=tk.Label(lmf,text='F_Name:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=1, column=0, pady=15, padx=20)

e=tk.Entry(lmf, bg='white', fg='black')
e.grid(row=1, column=1)



l=tk.Label(lmf,text='L_Name:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=2, column=0, pady=15, padx=20)

e=tk.Entry(lmf, bg='white', fg='black')
e.grid(row=2, column=1)


l=tk.Label(lmf,text='Class:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=3, column=0, pady=15, padx=20)

e=tk.Entry(lmf, bg='white', fg='black')
e.grid(row=3, column=1)



l=tk.Label(lmf,text='Stream:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=4, column=0, pady=15, padx=20)

e=tk.Entry(lmf, bg='white', fg='black')
e.grid(row=4, column=1)



l=tk.Label(lmf,text='E_Mail:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=5, column=0, pady=15, padx=20)

e=tk.Entry(lmf, bg='white', fg='black')
e.grid(row=5, column=1)




l=tk.Label(rmf,text='Python:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=0, column=0, pady=15, padx=20)

e=tk.Entry(rmf, bg='white', fg='black')
e.grid(row=0, column=1)



l=tk.Label(rmf,text='ML:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=1, column=0, pady=15, padx=20)

e=tk.Entry(rmf, bg='white', fg='black')
e.grid(row=1, column=1)



l=tk.Label(rmf,text='SQL:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=2, column=0, pady=15, padx=20)

e=tk.Entry(rmf, bg='white', fg='black')
e.grid(row=2, column=1)



l=tk.Label(rmf,text='Percentage:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=3, column=0, pady=15, padx=20)

e=tk.Entry(rmf, bg='white', fg='black')
e.grid(row=3, column=1)


l=tk.Label(rmf,text='Grade:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=4, column=0, pady=15, padx=20)

e=tk.Entry(rmf, bg='white', fg='black')
e.grid(row=4, column=1)


l=tk.Label(rmf,text='Total:', bg='yellow', fg='black', font=('purisa', 10, 'bold'), width=17)
l.grid(row=5, column=0, pady=15, padx=20)

e=tk.Entry(rmf, bg='white', fg='black')
e.grid(row=5, column=1)



def show():
    with open('E:\\python learning\\infoysy.txt'+sid.get()+'.txt','w') as file:
        file.write(sid.get()+','+ 
                   f_name.get()+','+ 
                   l_name.get()+','+
                   clss.get()+','+
                   stream.get()+','+
                   email.get())
    tk.messagebox.showinfo('http\redhatt.com', 'save your info.')
b=tk.Button(mf, bg='orange', fg='black', width=25, command=show, text='Save', font=('purisa', 15, 'bold'))
b.place(x=460, y=415, width=85, height=35)



def clear():
    sid.set(' ')
    f_name.set('')
    l_name.set('')
    clss.set('')
    stream.set('')
    email.set('')
    python.set('')
    sql.set('')
    ml.set('')
    total.set('')
    grade.set('')
    percentage.set('')
b1=tk.Button(mf, text='Clear', bg='orange', fg='black', width=25, command=clear, font=('purisa', 15, 'bold'))
b1.place(x=550, y=415, width=85, height=35)



def logout():
    ask=tk.messagebox.askyesno('http\redhatt.com', 'Warning, Do you really want to Exit!')
    if ask>0:
        top.destroy()
b1=tk.Button(mf, text='Logout', bg='orange', fg='black', width=25, command=logout, font=('purisa', 15, 'bold'))
b1.place(x=640, y=415, width=85, height=35)


top.mainloop()


       

#                  P r o j e  c  t  -  16


import tkinter
from tkinter import *
import tkinter as tk
top=tk.Tk()


top.geometry('800x500')
top.configure(bg='white')

tt=tk.Frame(bg='gray')
tt.place(x=425, y=50, width=750, height=235)

ttt=tk.Frame(bg='white')
ttt.place(x=475, y=73, width=650, height=190)

l=tk.Label(ttt, bg='cyan', fg='black', text='Mr/Ms:', width=15, font=('purisa', 10, 'bold'))
l.grid(row=0,column=0, padx=10, pady=12)

e=tk.Entry(ttt,bg='silver', fg='red', width=45)
e.grid(row=0,column=1)


l=tk.Label(ttt, bg='cyan', fg='black', text='std:', width=12, font=('purisa', 10, 'bold'))
l.grid(row=1,column=0, padx=5, pady=5)

e=tk.Entry(ttt,bg='silver', fg='red', width=16)
e.grid(row=1,column=1)


l=tk.Label(ttt, bg='cyan', fg='black', text='Div:', width=10, font=('purisa', 10, 'bold'))
l.grid(row=1,column=2, padx=5, pady=5)

e=tk.Entry(ttt,bg='silver', fg='red', width=15)
e.grid(row=1,column=3)



l=tk.Label(ttt, bg='cyan', fg='black', text='Town:', width=12, font=('purisa', 10, 'bold'))
l.grid(row=2,column=0, padx=2, pady=5)

e=tk.Entry(ttt,bg='silver', fg='red', width=16)
e.grid(row=2,column=1)



l=tk.Label(ttt, bg='cyan', fg='black', text='State:', width=10, font=('purisa', 10, 'bold'))
l.grid(row=2,column=2, padx=2, pady=5)

e=tk.Entry(ttt,bg='silver', fg='red', width=15)
e.grid(row=2,column=3)


l=tk.Label(ttt, bg='cyan', fg='black', text='Signature of Principle:', width=18, font=('purisa', 10, 'bold'))
l.grid(row=3,column=0, padx=10, pady=5)

e=tk.Entry(ttt,bg='silver', fg='red', width=45)
e.grid(row=3,column=1)

Div=tk.StringVar() 
def submit():
    c=tk.messagebox.askokcancel('COET', 'Information Submitted....')
    if c>0:
        top.destroy()

       
    with open('E:\python learning\mouse.txt', 'w') as file:
     file.write(Div.get())
     
b=tk.Button(ttt, text='Submit', command=submit, bg='red', fg='black', font=('purisa',15, 'bold'))
b.grid(row=4, column=3, pady=1)

top.mainloop()





#                  P r o j e  c  t  -  17

import tkinter
import tkinter as tk
from tkinter import *
top=tk.Tk()
top.configure(bg='silver')


def save_info():
    Username_info=Username.get()
    Password_info=Password.get()
    print(Username_info, Password_info)
    
    file=open('E://python learning//users.txt')
    file.write(Username_info)
    file.write(Password_info)
    file.close()
    print('User', Username_info, 'has been registered successfully')



# creation of variable
Username=StringVar()
Password=StringVar()


l=tk.Label(top, text='Username:', bg='silver', fg='black', font=('purisa', 10, 'bold'), width=15)
l.grid(row=0, column=0)

e=tk.Entry(top, bg='white', fg='red')
e.grid(row=0, column=1)


l=tk.Label(top, text='Password:', bg='silver', fg='black', font=('purisa', 10, 'bold'), width=15)
l.grid(row=1, column=0)

e=tk.Entry(top, bg='white', fg='red')
e.grid(row=1, column=1)




b=tk.Button(top, text='Save', command=save_info, bg='orange', fg='black', width=12)
b.grid(row=2, column=2)


def show():
    ask=tk.messagebox.askyesno('Warning', 'Do you Really want to Exit')
    if ask>0:
        top.destroy()
b1=tk.Button(top, text='Exit', command=show,  bg='orange', fg='black', width=12)
b1.grid(row=3, column=2)



top.mainloop()






#                  P r o j e  c  t  -  18

import tkinter as tk
from tkinter import *
top=tk.Tk()

top.configure(bg='pink')
top.geometry('500x500')

l=tk.Label(top, text='Fnme', bg='pink', fg='black', width=10,font=('purisa', 10, 'bold'))
l.grid(row=0, column=0, pady=10)

e=tk.Entry(bg='white', fg='red')
e.grid(row=0, column=1)


l=tk.Label(top, text='Lnme', bg='pink', fg='black' ,width=10,font=('purisa', 10, 'bold'))
l.grid(row=1, column=0)

e=tk.Entry(bg='white', fg='red')
e.grid(row=1, column=1)


laptop_comp=['Acer', 'Dell', 'MacBook', 'Asus', 'Lenovo', 'HP', 'Apple', 'Sony']
c=IntVar()
laptop_comp=OptionMenu(top, c, *laptop_comp)
laptop_comp.configure(width=10,bg='green')
c.set('Select')
laptop_comp.grid(row=2, column=1, pady=7)


l=tk.Label(top, text='Customer_gender:', bg='pink', fg='black', width=19, font=('purisa', 10, 'bold'))
l.grid(row=3, column=0, padx=20)


c1=StringVar()
C1=Checkbutton(top, text='Male', bg='orange', fg='black')
C1.grid(row=3, column=1, pady=8)

c2=Radiobutton(top, text='Female', bg='orange', fg='black')
c2.grid(row=4, column=1)

top.mainloop()





#                  P r o j e  c  t  -  19

from tkinter import *
import tkinter as tk
top=tk.Tk()

top.configure(bg='silver')
top.geometry('500x500')
top.title('Result\nmu.com')

mf=tk.Frame(top, bg='orange')
mf.place(x=250, y=40, width=420, height=270)

l=tk.Label(mf, text='PRN No:', bg='white', fg='black', width=12)
l.grid(row=0, column=0, pady=10, padx=165)

e=tk.Entry(mf, bg='white', fg='red')
e.grid(row=1, column=0, padx=158)

branchlst=['EE', 'IT', 'CE', 'ME', 'CsE', 'CmE', 'AE', 'EEE']
c=IntVar()
c.set('select')
branchlst=OptionMenu(mf, c, *branchlst)
branchlst.configure( bg='green')
branchlst.place(x=175, y=72)

Genderlst=['Male', 'Female', 'Other']
c1=IntVar()
c1.set('Select')
Genderlst=OptionMenu(mf,c, *Genderlst)
Genderlst.configure(bg='maroon')
Genderlst.place(x=175, y=110)

ll=tk.Label(mf, text='Here, press the button, if the above info is Correct..!', bg='orange', fg='black', font=('purisa', 10, 'bold'))
ll.place(x=60, y=160)

var=StringVar()
c=Checkbutton(mf,variable=var, bg='orange', width=11)
c.place(x=34, y=190)

def exit():
    ask=tk.messagebox.askyesno('Warning', 'Do you want to exist the page?')
    if ask>0:
        top.destroy()
        
b=tk.Button(mf, text='Exit', command=exit, bg='gray', fg='white', width=12, font=('purisa', 10, 'bold'))
b.place(x=250, y=210)
top.mainloop()






#                  P r o j e  c  t  -  20


import tkinter as tk
from tkinter import *
from tkinter import filedialog
top=tk.Tk()
top.configure(bg='cyan')
top.geometry('500x500')


f=tk.Frame(top, bg='gray')
f.place(width=500, height=300, x=510, y=70)

l=tk.Label(f, text='Username/PRN', bg='black', fg='red', font=('purisa', 10, 'bold'))
l.grid(row=0, column=0, padx=50, pady=25)

e=tk.Entry(f, bg='white', fg='red')
e.grid(row=0, column=1)


l=tk.Label(f, text='Password', bg='black', fg='red', font=('purisa', 10, 'bold'))
l.grid(row=1, column=0 )

e=tk.Entry(f, bg='white', fg='red')
e.grid(row=1, column=1)

lst=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
c=IntVar()
c.set('Put Roll No:')
droplst=OptionMenu(f, c, *lst)
droplst.configure(bg='lightblue')
droplst['menu'].configure(bg='red', fg='black')
droplst.grid(row=2, column=1, pady=10)



l=tk.Label(f, text='Gender', bg='black', fg='red', font=('purisa', 10, 'bold'))
l.grid(row=3, column=0 )

var=IntVar()
c=tk.Checkbutton(f, text='Male',variable=var,  bg='green' ,fg='black')
c.grid(row=3, column=1)

var1=IntVar()
c1=tk.Checkbutton(f, text='Female', variable=var1, bg='green', fg='black')
c1.grid(row=3, column=2)


def file_opener():
    intput=filedialog.askopenfile(initialdir="/")
    print(intput)
    for i in intput:
        print(i)
        
c=tk.Button(f, text='Upload the file', bg='red', fg='white', command=lambda:file_opener())
c.grid(row=5, column=1, pady=20)



def exist():
    ask=tk.messagebox.askyesnocancel('Warning', 'Do you want exist the page?')
    if ask>0:
        top.destroy()
v=tk.Button(f, text='Exist', command=exist, bg='orange', fg='black', width=15)
v.grid(row=6, column=2)
top.mainloop()





#                  P r o j e  c  t  -  21


import tkinter as tk
from tkinter import *
top=tk.Tk()
top.configure(bg='blue')
top.geometry('500x500')

f=tk.Frame(top, bg='silver')
f.place(x=510, width=400, height=350,y=50)

l=tk.Label(f, text='Enter Name', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=0, column=0, pady=12)


e=tk.Entry(f, bg='white', fg='black')
e.grid(row=0, column=1)


l=tk.Label(f, text='Enter Email', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=1, column=0, pady=10)


e=tk.Entry(f, bg='white', fg='black')
e.grid(row=1, column=1)


l=tk.Label(f, text='Contact Number', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=2, column=0,pady=10)


e=tk.Entry(f, bg='white', fg='black')
e.grid(row=2, column=1)


l=tk.Label(f, text='Select Gender', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=3, column=0)

var=IntVar()
c=tk.Checkbutton(f, text='Male', variable=var, bg='silver', fg='black')
c.grid(row=3, column=1)


var1=IntVar()
c=tk.Checkbutton(f, text='Female', variable=var1, bg='silver', fg='black')
c.grid(row=3, column=2)



l=tk.Label(f, text='Select Code', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=4, column=0, pady=10)

lst=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
c=IntVar()
c.set('Country Code')
droplst=OptionMenu(f, c, *lst)
droplst.configure(bg='red')
droplst['menu'].configure(bg='pink')
droplst.grid(row=4, column=1)




l=tk.Label(f, text='Enter Password', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=5, column=0, pady=10)


e=tk.Entry(f, bg='white', fg='black')
e.grid(row=5, column=1)


l=tk.Label(f, text='Re-Enter Password', bg='silver', fg='black', font=('purisa', 10, 'bold'))
l.grid(row=6, column=0, pady=10, padx=10)


e=tk.Entry(f, bg='white', fg='black')
e.grid(row=6, column=1)


def register():
    tk.messagebox.showinfo('Please Register!!!')
c=tk.Button(f, text='Register', command=register, bg='silver', fg='black', width=11)
c.grid(row=7, column=2, pady=15)


top.mainloop()

