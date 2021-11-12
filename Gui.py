# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:11:40 2021

@author: acer
"""

import tkinter as tk
    
root=tk.Tk()

root.title('Info 2.0')
root.geometry('1350x650')
root.config(bg='cyan')
top_frame=tk.Frame(root,bg='#bc1800')
top_frame.place(x=5,y=5,width=1340,height=150)
left_frame=tk.Frame(root,bg='#bc1800')
left_frame.place(x=5,y=160,width=667,height=380)
right_frame=tk.Frame(root,bg='#bc1800')
right_frame.place(x=678,y=160,width=667,height=380)
bottom_frame=tk.Frame(root,bg='#bc1800')
bottom_frame.place(x=5,y=545,width=1340,height=100)

#Create variable :

sid=tk.StringVar()
f_name=tk.StringVar()
l_name=tk.StringVar()
clss=tk.StringVar()
stream=tk.StringVar()
email=tk.StringVar()
python=tk.IntVar()
r=tk.IntVar()
ml=tk.IntVar()
total=tk.IntVar()
percentage=tk.IntVar()
grade=tk.IntVar()

#Create msgbox :

def logout():
    ask=tk.messagebox.askyesno('Warning','Do you really want to logout')
    if ask>0:
        root.destroy()

def clear():
        sid.set('')
        f_name.set('')
        l_name.set('')
        clss.set('')
        stream.set('')
        email.set('')
        python.set('')
        r.set('')
        ml.set('')
        total.set('')
        percentage.set('')
        grade.set('')
        


def calculate():
    tot=python.get()+ml.get()+r.get()
    total.set(tot)
    per=(tot/300)*100
    percentage.set(per)
    
    
    if per>=95:
        grade.set('O')   
    elif per<=95 and per>=85: 
        grade.set('A')
    elif per<85 and per>75:
        grade.set('B')
    elif per<75 and per>65:
        grade.set('C')
    elif per<65 and per>50:
        grade.set('D')  
    elif per<45:
        grade.set('F')    
    else:
        grade.set('F')
        
        
           
        
def save():
    calculate()
    with open('E:\\python learning\\infoysy.txt'+sid.get()+'.txt','w') as file:
        file.write(sid.get()+','+ 
                   f_name.get()+','+ 
                   l_name.get()+','+
                   clss.get()+','+
                   stream.get()+','+
                   email.get())
                                   
        
                   

#Create Label left side :

title_lbl=tk.Label(top_frame,text='Result 2.0',font=('Times new Roman',40,'bold'),bg='gray',fg='black')
title_lbl.pack(pady=50)                           
left_title_lbl=tk.Label(left_frame,text='P_Info :',font=('Times new Roman',25),bg='cyan')
left_title_lbl.grid(row=0,column=0)

id_lbl=tk.Label(left_frame,text='ID :',font=('Times new Roman',20),bg='#bc1800', fg='white')
id_lbl.grid(row=1,column=0,sticky=tk.W)                 #'W' as a constant It means west side
id_txt=tk.Entry(left_frame,text=sid,font=('Times new Roman',20))
id_txt.grid(row=1,column=1)

f_name_txt_lbl=tk.Label(left_frame,text='F_Name :',font=('Times new Roman',20),bg='#bc1800', fg='white')
f_name_txt_lbl.grid(row=2,column=0,sticky=tk.W)                 
f_name_entry=tk.Entry(left_frame,text=f_name,font=('Times new Roman',20))
f_name_entry.grid(row=2,column=1)

l_name_txt_lbl=tk.Label(left_frame,text='L_Name :',font=('Times new Roman',20),bg='#bc1800', fg='white')
l_name_txt_lbl.grid(row=3,column=0,sticky=tk.W)                 
l_name_entry=tk.Entry(left_frame,text=l_name,font=('Times new Roman',20))
l_name_entry.grid(row=3,column=1)

class_txt_lbl=tk.Label(left_frame,text='Class :',font=('Times new Roman',20),bg='#bc1800', fg='white')
class_txt_lbl.grid(row=4,column=0,sticky=tk.W)                 
class_entry=tk.Entry(left_frame,text=clss,font=('Times new Roman',20))
class_entry.grid(row=4,column=1)

stream_txt_lbl=tk.Label(left_frame,text='Stream :',font=('Times new Roman',20),bg='#bc1800', fg='white')
stream_txt_lbl.grid(row=5,column=0,sticky=tk.W)                 
stream_entry=tk.Entry(left_frame,text=stream,font=('Times new Roman',20))
stream_entry.grid(row=5,column=1)

email_txt_lbl=tk.Label(left_frame,text='Email :',font=('Times new Roman',20),bg='#bc1800', fg='white')
email_txt_lbl.grid(row=6,column=0,sticky=tk.W)                 
email_entry=tk.Entry(left_frame,text=email,font=('Times new Roman',20))
email_entry.grid(row=6,column=1)


#Right Side :

right_title_lbl=tk.Label(right_frame,text='M_Info :',font=('Times new Roman',25),bg='cyan')
right_title_lbl.grid(row=0,column=0)

python_txt_lbl = tk.Label(right_frame, text= 'Python :',font = ('Times New Roman',20),bg='#bc1800', fg='white')
python_txt_lbl.grid(row=1, column=0,sticky=tk.W)
python_entry =tk.Entry(right_frame,textvariable=python,font = ('Times New Roman',20))
python_entry.grid(row=1, column=1)

r_txt_lbl = tk.Label(right_frame, text= 'R :',font = ('Times New Roman',20),bg='#bc1800', fg='white')
r_txt_lbl.grid(row=2, column=0,sticky=tk.W)
r_entry =tk.Entry(right_frame,text=r,font = ('Times New Roman',20))
r_entry.grid(row=2, column=1)

ML_txt_lbl = tk.Label(right_frame, text= 'ML :',font = ('Times New Roman',20),bg='#bc1800', fg='white')
ML_txt_lbl.grid(row=3, column=0,sticky=tk.W)
ML_entry =tk.Entry(right_frame,text=ml,font = ('Times New Roman',20))
ML_entry.grid(row=3, column=1)

total_txt_lbl = tk.Label(right_frame, text= 'Total :',font = ('Times New Roman',20),bg='#bc1800', fg='white')
total_txt_lbl.grid(row=4, column=0,sticky=tk.W)
total_entry =tk.Entry(right_frame,text=total,font = ('Times New Roman',20))
total_entry.grid(row=4, column=1)

per_txt_lbl = tk.Label(right_frame, text= 'Percentage :',font = ('Times New Roman',20),bg='#bc1800', fg='white')
per_txt_lbl.grid(row=5, column=0,sticky=tk.W)
per_entry =tk.Entry(right_frame,text=percentage,font = ('Times New Roman',20))
per_entry.grid(row=5, column=1)

grade_txt_lbl = tk.Label(right_frame, text= 'Grade :',font = ('Times New Roman',20),bg='#bc1800', fg='white')
grade_txt_lbl.grid(row=6, column=0,sticky=tk.W)
grade_entry =tk.Entry(right_frame,text=grade,font = ('Times New Roman',20))
grade_entry.grid(row=6, column=1)

#Create Buttons in bottom frame :

save_btn=tk.Button(bottom_frame,command=save,text='Save',font=('Times New Roman',20),bg='orange',fg='white')
save_btn.pack(pady=30,side=tk.RIGHT,padx=5)

clear_btn=tk.Button(bottom_frame,command=clear,text='Clear',font=('Times New Roman',20),bg='orange',fg='white')
clear_btn.pack(pady=30,side=tk.RIGHT,padx=5)

quit_btn=tk.Button(bottom_frame,command=logout,text='Quit',font=('Times New Roman',20),bg='orange',fg='white')
quit_btn.pack(pady=30,side=tk.RIGHT,padx=5)



root.mainloop()
 
