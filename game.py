# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:49:52 2021

@author: Patil
"""

import random
play_again = True
wallet = 0
while play_again:
    if wallet < 9:
        amount = int(input("kindly recharge with min Rs.10 or more: "))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            c_guess = random.randint(1, 10)
            for chance in range(1, 4):
                u_guess = int(input("kindly enter your guess from 1 to 10: "))
                if c_guess == u_guess:
                    print("congratz...you have guessed correctly")
                    if chance == 1:
                        print("you have won Rs.100")
                        wallet += 100
                    elif chance == 2:
                        print("you have won Rs.50")
                        wallet += 50
                    else:
                        print("you have won Rs.25")
                        wallet += 25
                        break
                elif c_guess > u_guess:
                    print("number is lower than u_guess")
                    if chance == 3:
                        print("you loss the game")
                        print("i was thinking of a number", c_guess)
                    else:
                        if chance == 3:
                            print("you loss the game")
                            print("i was thinking of a number", c_guess)
                        if chance == 3:
                            print("you loss the game")
                            
    choice = input("Do you want to play again [yes/no]: ")
    if choice =="no":
        play_again = False
        withdrawn = input("do you want to withdraw [ yes/no]: ")
        if withdrawn == "yes":
            withdrawl_amt = int(input("kindly enter the amount: "))
            if withdrawl_amt > wallet:
                print('Insufficient amount')
            else:
                print("f{withdrawl_amt} transffered to your bank account.")
                wallet -= withdrawl_amt







import random
play_again = True
wallet = 0
while play_again:
    if wallet < 9:
        amount = int(input("kindly recharge with min Rs.10 or more: "))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            c_guess = random.randint(1, 10)
            for chance in range(1, 4):
                u_guess = int(input("kindly enter your guess from 1 to 10: "))
                if c_guess == u_guess:
                    print("congratz...you have guessed correctly")
                    if chance == 1:
                        print("you have won Rs.100")
                        wallet += 100
                    elif chance == 2:
                        print("you have won Rs.50")
                        wallet += 50
                    else:
                        print("you have won Rs.25")
                        wallet += 25
                        break
                elif c_guess > u_guess:
                    print("no is lower than u_guess")
                    if chance == 3:
                     print("you loss the game")
                     print("i was thinking of a number", c_guess)
                else:
                    
                     if chance == 3:
                        print("you loss the game")
                        print("i was thinking of a number", c_guess)
                     if chance == 3:
                        print("you loss the game")
    choice = input("Do you want to play again [yes/no]: ")
    if choice !="yes":
        play_again = False
        withdrawn = input("do you want to withdraw [ yes/no]: ")
        if withdrawn == "yes":
            withdrawl_amt = int(input("kindly enter the amount: "))
            if withdrawl_amt > wallet:
                print('Insufficient amount')
            else:
                print("f{withdrawl_amt} transffered to your bank account.")
                wallet -= withdrawl_amt


import random
play_again=True
wallet = 0
while play_again:
    if wallet < 9:
        amount=int(input("recharge with min Rs.10 or more: "))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            c_guess=random.randint(1, 10)
            for chance in range(1,4):
                u_guess=int(input("kindley you have guess from 1 to 10: "))
                if c_guess==u_guess:
                    print("congratz..you have guess correctly")
                    if chance == 1:
                        print("you won Rs.100")
                        wallet += 100
                    elif chance == 2:
                        print("you won Rs.50")
                        wallet += 50
                    else:
                        print("you won Rs.25")
                        wallet += 25
                        break
                elif c_guess > u_guess:
                    print("no lower than u_guess")
                    if chance == 3:
                        print("you loss the game")
                        print("i was thinking of a number", c_guess)
                    else:
                        if chance == 3:
                            print("you loss the game")
                            print("i was thinking of a number", c_guess)
                        if chance == 3:
                            print("you loss the game")
        choice=input("Do you want to play again [yes/no] :")                    
        if choice !="yes":
            play_again=False
            withdrawn=input("Do you want to withdrawn [yes/no] :")
            if withdrawn =="yes":
                withdrawl_amt=int(input("enter a amount"))
                if withdrawl_amt > wallet:
                    print("Insufficient amount")
                else:
                    print("f{withdrwal_amt} transferred amount to your bank account.")
                    wallet -= withdrawl_amt
             
                        


import random
play_again=True
wallet = 0
while play_again:
    if wallet < 9:
        amount=int(input("recharge with min Rs.10 or more: "))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            c_guess=random.randint(1, 10)
            for chance in range(1,4):
                u_guess=int(input("kindley you have guess from 1 to 10: "))
                if c_guess==u_guess:
                    print("congratz..you have guess correctly")
                    if chance == 1:
                        print("you won Rs.100")
                        wallet += 100
                    elif chance == 2:
                        print("you won Rs.50")
                        wallet += 50
                    else:
                        print("you won Rs.25")
                        wallet += 25
                        break
                elif c_guess > u_guess:
                        print("no is lower than u_guess")
                        if chance == 3:
    
                            print("you loss the game")
                            print("i was thinking of a number", c_guess)
                        else:
                            if chance == 3:
                                print("you loss the game")
                                print("i was thinking of a number", c_guess)
                            if chance == 3:
                                print("you loss the game")
        choice=input("Do you want to play again [yes/no] :")                    
        if choice !="yes":
            play_again=False
            withdrawn=input("Do you want to withdrawn [yes/no] :")
            if withdrawn =="yes":
                withdrawl_amt=int(input("enter a amount"))
                if withdrawl_amt > wallet:
                    print("Insufficient amount")
                else:
                    print("f{withdrwal_amt} transferred amount to your bank account.")
                    wallet -= withdrawl_amt
                                  
    import random
    c_guess=random.randint(1, 10) 
    for chance in range(1,4):
        u_guess=int(input("enter a guess no: "))
        if c_guess==u_guess:
            print("congratz..you have guessed")
            break
            if chance == 1:
               print("you won Rs.100")
            elif chance == 2:
               print("you won Rs.50")
        else:
            if chance == 3:
               print("you won Rs.25")
               print("sorry , you wrong guessed")
    print("i was thinking of a number", c_guess)
     






#3_chance
import random
c_guess=random.randint(1, 5) 
for chance in range(1,4):
    u_guess=int(input("enter a guess no: "))
    if c_guess==u_guess:
        print("congratz..you have guessed")
    else:
        print("sorry , you wrong guessed")
print("i was thinking of a number", c_guess)
        
        
#reward
import random
c_guess=random.randint(1, 5) 
for chance in range(1,3):
        u_guess=int(input("enter a guess no: "))
        if c_guess==u_guess:
            print("congratz..you have guessed")
            if chance == 1:
               print("you won Rs.100")
            elif chance == 2:
               print("you won Rs.50")
        else:
               print("sorry , you wrong guessed")
print("i was thinking of a number", c_guess)
                                                                   




#Entry fees
import random
play_again=True
wallet = 0
while play_again:
        if wallet < 9:
            amount=int(input("recharge with min Rs.10 or more: "))
            wallet += amount
            if wallet > 9:
                wallet -= 10
                c_guess=random.randint(1, 5)
                for chance in range(1,4):
                    u_guess=int(input("kindley enter your have guseed from 1 to 5:"))
                    if c_guess==u_guess:
                        print("congratz..you have guessed correctly")
                        if chance == 1:
                            print("you won Rs.100")
                            wallet += 100
                        elif chance ==2:
                            print("you won Rs.50")
                            wallet += 50
                            break
                    else:
                            print("sorry, you have wrong  guessed")
                            print("i was thinking of a number", c_guess)
        choice=input("Do you want to play again [yes/no] :")
        if choice =="no":
           play_again=False


#withdrawl
import random
play_again=True
wallet = 0
while play_again:
        if wallet < 9:
            amount=int(input("recharge with min Rs.10 or more: "))
            wallet += amount
            if wallet > 9:
                wallet -= 10
                c_guess=random.randint(1, 5)
                for chance in range(1,4):
                    u_guess=int(input("kindley enter your have guseed from 1 to 5:"))
                    if c_guess==u_guess:
                        print("congratz..you have guessed correctly")
                        if chance == 1:
                            print("you won Rs.100")
                            wallet += 100
                        elif chance ==2:
                            print("you won Rs.50")
                            wallet += 50
                            break
                    else:
                            print("sorry, you have wrong  guessed")
                            print("i was thinking of a number", c_guess)
        choice=input("Do you want to play again [yes/no] :")
        if choice =="no":
          play_again=False
          withdrawn = input("do you want to withdraw [ yes/no]: ")
          if withdrawn == "yes":
            withdrawl_amt = int(input("kindly enter the amount: "))
            if withdrawl_amt > wallet:
                print('Insufficient amount')
            else:
                print("f{withdrawl_amt} transffered to your bank account.")
                wallet -= withdrawl_amt
             
    
    
#hints
import random
play_again=True
wallet = 0
while play_again:
        if wallet < 9:
            amount=int(input("recharge with min Rs.10 or more: "))
            wallet += amount
            if wallet > 9:
                wallet -= 10
                c_guess=random.randint(1, 5)
                for chance in range(1,4):
                    u_guess=int(input("kindley enter your have guseed from 1 to 5:"))
                    if c_guess==u_guess:
                        print("congratz..you have guessed correctly")
                        if chance == 1:
                            print("you won Rs.100")
                            wallet += 100
                        elif chance ==2:
                            print("you won Rs.50")
                            wallet += 50
                            break
                        elif c_guess > u_guess:
                            print("no is lower than u_guess")
                            if chance == 2:
                                print("you loss the game")
                                print("i was thinking of a number", c_guess)
                            
                    else:
                        if chance == 2:
                            print("you loss the game")
                            print("i was thinking of a number", c_guess)
        choice=input("Do you want to play again [yes/no] :")
        if choice =="no":
          play_again=False
          withdrawn = input("do you want to withdraw [ yes/no]: ")
          if withdrawn == "yes":
            withdrawl_amt = int(input("kindly enter the amount: "))
            if withdrawl_amt > wallet:
                print('Insufficient amount')
            else:
                print("f{withdrawl_amt} transffered to your bank account.")
                wallet -= withdrawl_amt
             
  #  chances 
   # reward
    # Entry fees
     # withdrawl
      # hints

#
import random
play_again=True
wallet = 0
while play_again:
        if wallet < 9:
            amount=int(input("recharge with min Rs.10 or more: "))
            wallet += amount
            if wallet > 9:
                wallet -= 10
                c_guess=random.randint(1, 5)
                for chance in range(1,4):
                    u_guess=int(input("kindley enter the guess from 1 to 5: "))
                    if c_guess==u_guess:
                        print("congratz..you have guess correctly")
                        if chance == 1:
                            print("you won Rs.100")
                            wallet += 100
                        elif chance == 2:
                            print("you won Rs.50")
                            wallet += 50
                        else:
                            print("you won Rs.25")
                            wallet += 25
                            break
                    elif c_guess > u_guess:
                            print("no is lower than u_guess")
                            if chance == 3:
                                print("you loss the game")
                                print("i was thinking of a number", c_guess)
                            else:
                                if chance == 3:
                                    print("you loss the game")
                                    print("i was thiking of a number", c_guess)
                                    if chance == 3:
                                        print("you loss the game")
        choice=input("Do you want to play again [yes/no]: ")
        if choice !="yes":
            play_again=False
            withdrawn=input("Do you want to withdrawn [yes/no]: ")
            if withdrawn =="yes":
                 withdrawl_amt=int(input("enter a amount"))
                 if withdrawl_amt > wallet:
                     print("Insufficient amount")
                 else:
                     print("f{withdrawl_amt} transferred amount to your bank account.")
                     wallet -= withdrawl_amt
#chance                            
import random
c_guess=random.randint(1, 10)
for chance in range(1,4):
    u_guess=int(input("enter the guess no :"))
    if c_guess==u_guess:
        print("congratz...you have correct guess")
    else:
        print("sorry, you have wrong guessed")
print("i was thinking of a number", c_guess)   
     
#rewards 
import random
c_guess=random.randint(1, 10)
for chance in range(1,4):
    u_guess=int(input("enter the guess no :"))
    if c_guess==u_guess:
        print("congratz...you have correct guess")
        if chance == 1:
            print("you won Rs.100")
        elif chance == 2:
            print("you won Rs.50")
        if chance == 3:
            print("you won Rs.25")
    else:
        print("sorry, you have wrong guessed")
print("i was thinking of a number", c_guess)

#entry fees
import random
play_again=True
wallet = 0
while play_again:
    if wallet < 9:
        amount=int(input("recharge with min Rs.10 or more :"))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            c_guess=random.randint(1, 10)
            for chance in range(1,4):
                u_guess=int(input("kindley enter the guess no: "))
                if c_guess==u_guess:
                    print("congratz..you have correct guessed")
                else:
                    print("sorry, you have wrong guessed")
        print("i was thinking of a number", c_guess)


              
# Number Guessing Game
import random
play_again=True
wallet = 0
while play_again:
    if wallet < 9:
        #entry fees
        amount=int(input("recharge with min Rs.10 or more: "))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            #chance
            c_guess=random.randint(1, 10)
            for chance in range(1,4):
                u_guess=int(input("kindley enter the guess no: "))
                if c_guess==u_guess:
                    print("congratz..you have guess from 1 to 10: ")
                    #reward
                    if chance == 1:
                        print("you won Rs.100")
                        wallet += 100
                    elif chance == 2:
                        print("you won Rs.50")
                        wallet += 50
                    else:
                        print("you won Rs.25")
                        wallet += 25
                        break
                    #hint
                elif c_guess > u_guess:
                        print("no is lower than u_guess")
                        if chance == 3:
                            print("you loss the game")
                            print("i was thinking of a number", c_guess)
                        elif chance == 3:
                            print("you loss the game")
                            print("i was thinking of a number", c_guess)
                        else:
                            if chance == 3:
                                print("you loss the game")
        choice=input("Do you want to play again [yes/no] :")
        if choice !="yes":
            play_again=False
            #withdraw
            withdrawn=input("Do you want to withdrawn [yes/no] :")
            if withdrawn == "yes":
                withdrawl_amt=int(input("enter a amount"))
                if withdrawl_amt > wallet:
                    print("Insufficient amount")
                else:
                    print("f{withdrawl_amt} transferred amount to your bank account.")
                    wallet -= withdrawl_amt                       





import random
play_again=True
wallet = 0
while play_again :
    if wallet < 9:
        amount=int(input('kindley recharge with 10 or more:'))
        c_guess=random.randint(1,5)
        for i in range(1,4):
            u_guess=int(input('Enter ure guess no:'))
            if c_guess==u_guess:
               
                if i==1:
                    print('Please collect ure Rs.100')
                    print('U won the first prize of the game.')
         
             
          
                elif i==2:
                        print('Please collect Rs.50')
                else:
                    print('Please collect Rs.25')
                                                
                    print('U won the third prize of the game')
            else:
                print('Sorry ! u have loss the game')
            if c_guess>u_guess:
                if i==1:
                    print('Number is lower than c_guess')
                elif i==2:
                    print('Number is lower  than c_guess')
                else:
                    print('Number is lower than c_guess')
                    print('I was thinking of number', c_guess)
    choice=input('Do u want play again [yes/no]:')

    






import random
play_again=True
wallet=0
while play_again:
    if wallet <9:
        Amount=int(input('Kindley Recharge with 10 or more:'))
        wallet += Amount
        c_guess=random.randint(1,5)
        for i in range(1,4):
            u_guess=int(input('Enter the guess no: '))
            if c_guess==u_guess:
                print('Congrtazz u have won the game.')
                if i==1:
                    print('Please collect Rs.1000')
                    print('U r won the first prize of the game.')
                elif i==2:
                    print('Please collect Rs.500')
                    print('U r won the second prize of the game.')
                else:
                     print('Please collect Rs.250')
                     print('U r won the third prize of the game.')
            elif c_guess>u_guess:
                if i==1:
                    print('Number is lower than c_guess')
                    print('Sorry! You loss the game.')
                elif i==2:
                     print('Number is lower than c_guess')
                     print('Sorry! You loss the game.')
                else:
                      print('Number is lower than c_guess')
                      print('Sorry! You loss the game.')
                      print('i was thinking of number', c_guess)
    choice=input('Do you want to play again [yes/no] :')
    if choice!='yes':
        play_again=False
        withdrwan=input('Do you want to withdrawn [yes/no] :')
        if withdrwan=='yes':
            withdrawl_amt=int(input('Withdrawl the amount :'))
            if withdrawl_amt>wallet:
                print('Insufficient balance in ure account')
            else:
                print(f'{withdrawl_amt} transffered amount to ure bank account.')
                wallet -= withdrawl_amt
            
            
 
        

my_string = 'data science class has started... seems like confusing'
my_string['0']='f'





# iterating
count = 0
for letter in 'Hello World how r you':
    if letter=="h":
        letter="W"
    print(letter, end =" ")
    
    count += 1 
    
print(count,'letters found')


count=0
for i in 'What is ure nme':
    if i=='i':
        i='A'
    print(i, end= ' ')
    count+=1
print(count, 'my nme is:')


import math
s=abs(math.sqrt(36))
print(s)
