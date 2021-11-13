# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:41:25 2021

@author: Patil
"""

#PYRAMID:-
def pattern(n):
    k=2*n-2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
                print("*", end=" ")
        print("\r")
pattern(10)


#INVERSE PYRAMID:-
def pattern(n):
    k=n-2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k=k+1
        for j in range(0, i+1):
                print("*", end=" ")
        print("\r")
pattern(10)


#RIGHT START PATTERN:-
def pattern(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
    for i in range(n, 0, -1):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")    
pattern(10)


#LEFT START PATTERN:-
def pattern(n):
    k=2*n-2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k=k-2
        for j in range(0, i+1):
            print("*",end=" ")
        print("\r")
    k=-1
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k=k+2
        for j in range(0, i+1):
             print("*", end=" ")            
        print("\r")
pattern(10)


#HOURGLASS:-
def pattern(n):
    k=n-2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k=k+1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
    k=2*n-2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
pattern(10)
            

#RIGHT:-
def pattern(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("*",end=" ")
        print("\r")
pattern(10)


#LFET:-
def pattern(n):
    k=2*n-2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k=k-2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
pattern(10)
        

#DOWNWARD HALF-PYRAMID:-
def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
pattern(10)
 
           
#HALF-DIAMOND SHAPE:-
def pattern(n):
    k=2*n-2
    for i  in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
pattern(10)
            

#FULL DIAMOND PATTERN:-
def pattern(n):
    k=2*n-2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
    k=n-2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k=k+1
        for j in range(0, i+1):
             print("*", end=" ")
        print("\r")
pattern(10)


#NUMBER DIAMOND SHAPE:-
def pattern(n):
    k=2*n-2
    x=0
    for i in range(0,n):
        x=x+1
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
                print(x, end=" ")
        print("\r")
    k=n-2
    x=0
    for i in range(n, -1, -1):
        x=x+1
        for j in range(k, 0, -1):
            print(end=" ")
        k=k+1
        for j in range(0, i+1):
                print(x, end=" ")
        print("\r")
pattern(7)
                
                
  
#DIAMOND SHAPE WITH  ALPHABETICAL CHARACTERS:-

def pattern(n):
    k=2*n-2
    x=65
    for i in range(0,n):
        ch=chr(x)
        x=x+1
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
                print(ch, end=" ")
        print("\r")
    k=n-2
    x=65
    for i in range(n, -1, -1):
        ch=chr(x)
        x=x+1
        for j in range(k, 0, -1):
            print(end=" ")
        k=k+1
        for j in range(0, i+1):
                print(ch, end=" ")
        print("\r")
pattern(7)
              
                      

#NUMBERS OF DOWNWARD HALF-PYRAMID:-
def pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("\r")
pattern(10)


#RIGHT ALPHABETICAL TRAINLE;-
def pattern(n):
    x=65
    for i in range(0, n):
        ch=chr(x)
        x=x+1
        for j in range(0, i+1):
            print(ch, end=" ")
        print("\r")
pattern(26)
    

       
#1
num=int(input('Enter the number of rows:'))
for i in range(1, num+1):
    print(' '*(num-i)+'*'*i)

#2
for i in range(4):
    for j in range(i-1):
        print('#', end=' ')
        print()
        
#3       
i=int(input('Enrer the row:'))
for i in range(i+1):
    print("vaibhav"*i)
         
           
    
#LAMBDA:-
def A(x):
    return (lambda y:x+y)
t=A(4)
print(t(8))
    

def A(x):
    return(lambda y:x+y)
t=A(4)
print(t(8))
u=A(7)
print(u(5))


#import calendar:-
from calendar import  calendar
Year=int(input('Enter the year: '))
print(calendar(Year))


