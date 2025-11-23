# Guessing game

import random as r

guess = r.randint(1, 100) # This value won't change
attempts = 10

def game():
    global attempts     # global varibale because this variable will change value

    print("*****")
    print("Guessing Number - Game")
    print("*****\n")

    while True:
        print(f"Attempts: {attempts}")
        ask = int(input(f"Which number i am thinking of ? \n"))
        if attempts != 0:

            if ask == guess:
                print("you got it!!")
                break
            elif abs(ask - guess) <= 5:
                print("You're close")
            elif ask < guess:
                print("too low")
            elif ask > guess:
                print("too high")
            else:
                print("ups! wrong... try again...\n")
        else:
            print("No more attempts")
            break

        attempts -= 1


game()
