# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:27:34 2021

@author: Patil
"""

# OOP's ( Object-Oriented Programming ):-
# Its used to repeated code by classes and object. OOP's help the often execute statements in thousand of lines.
# Better efficiency and maintain the code.
# Most Commonly topic in kinds of langauges (C, C++, Python, Ruby, PHP, Javascript, Java etc.)

class Student:
    def hello(self):
        print('Welcome to student class method')
s=Student()
s.hello()


#Addition:
class Arithmatic():
    def addition(self):    # self:- it's Standard  arguments uske jagah abc ya kuch bhi dal saktey hai....!
        a=int(input('Enter the num1:'))
        b=int(input('Enter the num2:'))
        return a+b
s=Arithmatic()
s.addition()


#Subtraction:
class Arithmatic():
    def substraction(self):
        a=int(input('Enter the num1:'))
        b=int(input('Enter the num2:'))
        
        sum=a-b
        return sum
c=Arithmatic()
c.substraction()

# 1)Mulplication:
class Arithamtic():
    def mul(self):
         a=int(input('Enter the num1:'))
         b=int(input('Enter the num2:'))
         
         sum=a*b
         return sum
     
d=Arithmatic()
d.mul()
        
#2):-
class Arithmatic():
    def mul(self):
        a=int(input('Enter the num1:'))
        b=int(input('Enter the num2:'))
        sum=a*b
        print(sum)
d=Arithmatic()
d.mul()


#Division:
class Arithmatic():
    def Division(self):
         a=int(input('Enter the num1:'))
         b=int(input('Enter the num2:'))
         sum=a/b
         print(sum)
v=Arithmatic()
v.Division()
        

#Constructor:-
#Two types of constructor:
#1) Non-Parameterized
#ex.

class Student:
    def __init__(self):  #------its Constructor
        print('Welcome to non-parameterized')
s=Student()


#2) Parameterized:-
class Student1:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def show(self):
        print('student name is', self.name, 'and marks is', self.marks)

s=Student1('vaibhav', 78)
s1=Student1('piyush',80)
s2=Student1('Sanjana', 77)
s.show()
s1.show()
s2.show()


#Defualt:-
class Student:
    name=' Mr.vaibhav Patil'
    age='21'
    height='5.78'
    destination='developer.'
    def show(self):
        print('Name is', self.name,', Age is', self.age,', Height is', self.height, 'and Destination is', self.destination)
    weight='55.'
    color='brown.'
    hairstyle='stud.'
    def display(self):
        print('student weight is', self.weight)
    def hello(self):
        print('student color is', self.color)
    def welcome(self):
        print('hairstyle of student is', self.hairstyle)
s=Student()
s.show()
s.display()
s.hello()
s.welcome()


# Destructor:- when your program ended then destructor used it and destructor deleted the objects that means free memory by oops (Destructor).
#Ex.

class Employees():
    def __int__(self):
        print('Employees Created.')
    def __del__(self):
        print('Employees Deleted.')
obj=Employees()
del obj






# Note:- In one class we can create multiple object.


#home-work:-
#print the fun student name & name of class:-
class Student:
    def __init__(self, student_name, student_class):
        self.student_name=student_name
        self.student_class=student_class
    def show(self):
        print('Student_Name is', self.student_name,'and Class is', self.student_class)
s=Student('vaibhav', 'T.E')
s.show()
      

#create empty class & check whether true or not:-
class Student1:
    pass
class Marks:
    pass
Student1=Student()
Marks1=Marks()
print(isinstance(Student1, Student))
print(isinstance(Marks1, Marks))
print(isinstance(Student1, Marks))
print('\ncheck whether the said classes are subclasses.')
print(issubclass(Student, object))
print(issubclass(Marks, object))

     
#class to implement pow(x,n):-
class py_solution:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x
        if x==-1:
            if n%2==0:
                return 1
            else:
                return 1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x, -n)
        val =self.pow(x, n//2)
        if n%2==0:
            return val*val
        return val*val*x
    
print(py_solution().pow(2, -3))
print(py_solution().pow(3, 5))
print(py_solution().pow(100, 0))


    
#class reverse a string word by word:-
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().reverse_words('Hello  .py'))
        

#find the radius & perimeter of circle:-
class Circle():
    def __init__(self, r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle=Circle(4)
print(NewCircle.area())
print(NewCircle.perimeter())


#Inheritance:-
#The child class property accquires the parent class.
#ex.
class Parent:
    def show(self):
        print('welcome to Parent class')
class Child(Parent):
    def display(self):
        print('welcome to Child class')
c=Child()
c.display()
c.show()


#multilevel Inheritance:-
# the parent class Accquires the property of grandparent class.
#ex.1
class Grandparent:
    def hello(self):
        print('welcome to Grandparent class')
class Parent(Grandparent):
    def show(self):
        print('welcome to Parent class')
class Child(Parent):
    def display(self):
        print('welcome to Child class')
c=Child()
c.display()
c.show()
c.hello()

#ex.2
class Railway:
    def hello(self):
        print('welcome to Railway class')
class Car(Railway):
    def show(self):
        print('Welcome to Car class')
class Bicycle(Car):
    def display(self):
        print('Welcome to Bicycle class')
o=Bicycle()
o.display()
o.show()
o.hello()





# Multiple / Hierarchical Inheritance:-
# The child class Accquires the property of both Father & Mother:-
#ex.1
class Father:
    def show(self):
        print('welcome to Father class')
class Mother:
    def display(self):
        print('welcome to Mother class')
class Child(Father, Mother):
    def hello(self):
        print('welcome to Child class')
c=Child()
c.show()
c.display()
c.hello()

#ex.2
class Cock:
    def show(self):
        print('welcome to cock class')
class Hen:
    def display(self):
        print('welcome to hen class')
class Little(Cock, Hen):
    def hello(self):
        print('Welcome to Little class')
l=Little()
l.show()
l.display()
l.hello()


#Addition using Multilevel inheritance:-
class First:
    def input(self):
        self.a=int(input("Enter the num1: "))
        self.b=int(input("Enter the num2: "))
class Second(First):
    def Add(self):
        self.z=self.a+self.b
class Third(Second):
    def result(self):
        print('sum of two num', self.z)
h=Third()
h.input()
h.Add()
h.result()


class First():
    def input(self):
        self.a=int(input('enter int1:'))
        self.b=int(input('enter int2:'))
class Second(First):
    def div(self):
        self.z=self.a/self.b
class Third(Second):
    def result(self):
        print('Division is', self.z)
z=Third()
z.input()
z.div()
z.result()






#Subtraction using Multilevel inheritance:-
class First:
    def input(self):
        self.a=int(input('Enter the num1: '))
        self.b=int(input('Enter the num2: '))
class Second(First):
    def sub(self):
        self.z=self.a-self.b
class Third(Second):
    def result(self):
        print('sub of two num', self.z)
v=Third()
v.input()
v.sub()
v.result()
    

#Multiplication using Multilevel inheritance:-
class First:
    def input(self):
        self.a=int(input('Enter the num1: '))
        self.b=int(input('Enter the num2: '))
class Second(First):
    def mul(self):
        self.z=self.a*self.b
class Third(Second):
    def result(self):
        print('mul of two num', self.z)
s=Third()
s.input()
s.mul()
s.result()
    




# Add
class one():
    def input(self):
        self.x=int(input('Enter in1:'))
        self.y=int(input('Ente rint2:'))
class two(one):
    def add(self):
        self.w=self.x+self.y
class three(two):
    def result(self):
        print('Addition is', self.w)
# sub
class four():
    def input(self):
        self.t=int(input('enter int1:'))
        self.v=int(input('enter int2:'))
class five(four):
    def sub(self):
        self.y=self.t-self.v
class six1(five):
    def result(self):
        print('substarction is', self.y)
#Mul
class First():
    def input(self):
        self.a=int(input('Enter int1:'))
        self.b=int(input('Enter int2:'))
class Second(First):
    def mul(self):
        self.z=self.a*self.b
class Third(Second):
    def result(self):
        print('Multification is', self.z)
#Div
class Forth():
    def input(self):
        self.c=int(input('Enter int1:'))
        self.d=int(input('enter int2:'))
class Fifth(Forth):
    def div(self):
        self.x=self.c/self.d
class Six(Fifth):
    def result(self):
        print('Division is', self.x)
        
# Modulus
class zero():
    def input(self):
        self.p=int(input('enter int1:'))
        self.o=int(input('enter in2:'))
class unic(zero):
    def Modulus(self):
        self.i=self.p//self.o
class xea(unic):
    def result(self):
        print('Modulus is', self.i)
w=three()
w.input()
w.add()
w.result()

y=six1()
y.input()
y.sub()
y.result()

z=Third()
z.input()
z.mul()
z.result()  
 
x=Six()
x.input()
x.div()
x.result()

i=xea()
i.input()
i.Modulus()
i.result()


a=int(input('int1:'))
b=int(input('enter in2:'))
print(a//b)




class Arithmatic():
    def add(self):
        self.a=int(input('Enter int1:'))
        self.b=int(input('Enter int2:'))
        return self.a+self.b
z=Arithmatic()
z.add()



class Student():
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def show(self):
        print('He is Name', self.name, 'And his Marks is', self.marks)
z=Student('Vaibhav', 88.)
z.show()


class Laptop():
    def show(self):
        print('Welcome to Laptop class')
class Tab(Laptop):
    def hello(self):
        print('Welcome to Tab class')
class Mo(Tab):
    def display(self):
        print('Welcome to mobile class')
l=Mo()
l.display()
l.hello()
l.show()



class Food():
    def hello(self):
        print('Welcome to Food class')
class Cloths():
    def display(self):
        print('Welcome to Cloths class')
class Shulter():
    def unic(self):
        print('Welcome to Shulter class')
class Human(Food, Cloths, Shulter):
    def show(self):
        print('Welcome to human class')
z=Human()
z.hello()
z.display()
z.unic()
z.show()



























#Division using Multilevel inheritance:-
# ex.1
class First:
    def input(self):
        self.a=int(input('Enter the num1: '))
        self.b=int(input('Enter the num2: '))
class Second(First):
    def div(self):
        self.z=self.a/self.b
class Third(Second):
    def result(self):
        print('div of two num', self.z)
j=Third()
j.input()
j.div()
j.result()
        

#ex.2
class A:
    def input(self):
        self.x=int(input('Enter the num1:  '))
        self.y=int(input('Enter the num2:  '))
class B(A):
    def Div(self):
        self.z=self.x/self.y
class C(B):
    def result(self):
        print('div of two num', self.z)
d=C()
d.input()
d.Div()
d.result()        











#Polymorphism:-
# Having many forms is called Polymorphism.
#ex.
len('Jesson') #------String

len([10,20,30]) #------List

len((1,2,3,4))  #-------Tuple

len({'john', 'Nargis'}) #------- Dict



# Encapsulation:-
# Wrapping the data.
# Ex.Medicine Capsule.
# Defin:- Several mixed data=Variables & Methods in single unit & these unit wrapping by encapsulation thats the data hiding.
# why importants? ----- Encapsulation provides security by hiding the data from the outside world.
# Get fun will be used for reading the data in encapsulation.
# Set fun will be used for writing the data in encapsulation.



















# Abstraction:-
# Hiding the un-wanted data./ One Class of Data is hide another class of data.
# Why important?--- to hide the data/class in order to reduce the complexity and efficiency of application. Abstraction can be achieved Python Program by using classes.
# ex. Car -- Model, Speed, Accelerate , Brake























# Exception:-
 # It is nothing but Error handling is called exception.
 # To handle te error we use try & except method.

#ZeroDivisionError:
num1=int(input('Enter the num1: '))
num2=int(input('Enter the num2: '))
try: 
    num1=num1/num2
except ZeroDivisionError:
        print('division by zero')
print('div is', num1)


#ValueError:
try:
    num1=int(input('Enter the num1: '))
    num2=int(input('Enter the num2: '))
    num1=num1/num2
except ValueError:
    print('Division by zero')
except ValueError:
    print('Enter the number')
print('div is', num1)



# Error:
try:
    num1=int(input('Enter the num1: '))
    num2=int(input('Enter the num2: '))
    
    num1=num1/num2
except:
    print('error')
print('div is', num1)


#Find out which type of error:
try:
    num1=int(input('Enter the num1: '))
    num2=int(input('Enter the num2: '))
    
    num1=num1/num2
except Exception as e:
    print('error', e)
print('div is', num1)


for i in range(2,5):
    a=int(input('Enter a num1:'))
    b=int(input('Enter a num2:'))
try:
    print('Dividion by two num is:, a/b')
except ZeroDivisionError as e:
    print('cannot divided by zero')


# For ValueError:
for i in range(2,5):
    try:
         a=int(input('Enter a num:'))
         b=int(input('Enter a num:'))
         print('the division of two num: a/b')
    except ZeroDivisionError as e:
        print('cannot divided bt zero')
    except ValueError as e:
        print('Kindley enter a valid input')
    except Exception as e:
        print(e)
    finally:
        print('I am always executed')
        
        
#-------------------------------------------------       
def reverse(str):
    str=str[::-1]
    return str
s='Seven Mentor'
print(s)
print(reverse(s))
    
     
def unic(str):
    str1=str[::-1]
    return str1

s='Seven Mentor'
print(s)
print(reverse(s))
    




# Add two numbers
a=int(input('Enter int1:'))
b=int(input('Enter int2:'))
c=a+b
print(c)

a=int(input('Enter int1:'))
b=int(input('Enter int2:'))
print(a+b)


a=int(input('enter int1:'))+int(input('enter int2:'))
print(a)

# check the even or odd number
for i in range(0,21):
    if i%2==0:
        print('Number is even')
    else:
        print('Number is odd')
print(i)


#make calculator using switch case
def switch():
    a=int(input('enter int1:'))
    b=int(input('Enter int2:'))
    print('Press 1 for addition\npress 2 for substraction \npress 3 fro multification \n press 4 for division')
    option=int(input('enter your option:'))
    if option==1:
        result=a+b
        print('Addition is', result)
    elif option==2:
         result=a-b
         print('Substarction is', result)
    elif option==3:
          result=a*b
          print('multifiaction is', result)
    elif option==4:
           result=a/b
           print('Division is', result)
    else:
        print('Invalid numbers')
switch()
        

#reverse number
str=[1,2,4,5,5,8,5889,49,9,9,79464]
b=str[::-1]
print(b)


# calculate sum of digits

a=[78,50,40,20,30]
total=sum(a)
print(total)

# calculate sum of digits and avg.

a=[78,50,40,20,30]
avg=sum(a)/len(a)
print(avg)
import math
print(round(avg,1))
print(math.ceil(avg))# catch max value.
print(math.floor(avg)) # catch min value.


# check a number palindrome or not.
str1=input('Enter a Str1:')
str2=str1[::-1]
if str1==str2:
    print('string is Palindrome.')
else:
    print('Is not Palindrome.')
    
    

# check N natural number
number=10;
for num in  range(1, number):
    print(num)
    
    
# check number is perfect or not
n=6
mysum=0
for i in range(1,n):
    if n%i==0:
        my=mysum+i
if my==n:
    print('Perfect number')
else:
    print('Is not perfect number')
    
    
    


#check prime number or not
num=int(input('enter number:'))
if num>1:
    for i in range(2, num):
        if num%i==0:
            print('Is not prime number')
            break
    else:
        print('Prime number')
        

# check the perfect the number or not
add=0
num=int(input('enter a number:'))
for i in range(1, num):
    if num%i==0:
        add=add+i
    if   num==add:
            print('Is perfect number.')
else:
            print('Isnot perfect number.')
        













# Addition by using lambda fun 

#tot=lambda a,b : a+b
#print(tot(10,20))

    
    
        