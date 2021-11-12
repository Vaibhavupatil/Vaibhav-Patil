 # Guessing Usser Numbers to Consider Machine number...!
    
  # Random=  id defined as varying the numbers every time.
import random
play_again = True
wallet = 0
while play_again:
    if wallet < 9:
        # Recharge the balance if less than Rs.> 9.0
        amount = int(input("kindly recharge with min Rs.10 or more: "))
        wallet += amount
        if wallet > 9:
            wallet -= 10
            # Chances
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
                    # Hints
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
    # Often play the game...!                        
    choice = input("Do you want to play again [yes/no]: ")
    if choice =="no":
        play_again = False
        # Withdraw the amount.
        withdrawn = input("do you want to withdraw [ yes/no]: ")
        if withdrawn == "yes":
            withdrawl_amt = int(input("kindly enter the amount: "))
            if withdrawl_amt > wallet:
                print('Insufficient amount')
            else:
                print("f{withdrawl_amt} transffered to your bank account.")                 # Transsfered amounts to your account.
                wallet -= withdrawl_amt

