# Casino game | Machine Game

# Numbers must match

# 7 7 7 wins extra

# If only 2 digits match, earns some money

# User must bet money

import random
import os

money = 0
bet = 0

def clear():
    os.system("clear")

def shuffle():
    r = random.randint(1,9)
    return r

def display(match):
    print("********************")
    print(f"Remaining money: {money}")
    print(f'Current bet: {bet}')
    print(match)    
    print("********************")

def match_conditions(match,money,bet):
    if match[0] == 7 and match[1] == 7 and match[2] ==7:
        print('7 lucky !!')
        money += bet * 10
        print(f"You've won {bet*10}")
        
    elif match[0] == match[1] == match[2]:
        print("Triple match!")
        money += bet * 5
        print(f"You've won {bet*5}")
        
    elif match[0]==match[1] or match[1] == match[2] or match[0] == match[2]:
        print("Double match!")
        money += bet * 2
        print(f"You've won {bet*2}")
        
    else:
        print('No match...')

    return money

def reset_attempts(gap):
    global bet
    if gap == 5:
        gap = 0
        change_bet = input("do you want to change the bet? y/n")
        if change_bet == "y":
            ask = int(input("how much do you want to bet?"))
            if ask > money:
                print("Must not exceed your total money. Try again")
            else:
                bet = ask
    return gap

def game():
    global money, bet
    gap = 0

    ask = int(input('how much money would you like to add?: '))
    if ask < 1:
        print('The money ammount must be greater than 1... try again.')
    else:
        money = ask
        ask = int(input("how much do you want to bet?"))
        if ask > money:
            print('Must not exceed your total money. Try again')
        else:
            bet = ask

        while money > 0:
            gap += 1
            if money < 0:
                print("You have run out of money...")
                break

            match = [shuffle(),shuffle(),shuffle()]
            
            display(match)

            money -= bet

            money = match_conditions(match,money,bet)

            ask = input('Continue? y/n')

            gap = reset_attempts(gap)
                        

            clear()
            if ask == 'n':
                break

game()
