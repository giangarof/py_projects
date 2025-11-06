# Create a rock paper scissor game

# Hint
# You might use random module
# You might use loops or match/case

import random

print("***        Game          ***")
print("*** Rock, Paper, Scissor ***")

start = True
score = {"computer": 0, "player": 0}
options = ["Rock", "Paper", "Scissor"]
player = ""

def scores():
    print("*****")
    print("Score")
    print(f"Player1: {score['player']} - Computer:{score['computer']}")
    print("*****")


def continue_game(num, player):
    q = input(f" {player} has reached {num} point \n Do you want to continue? Y/N")
    if q == "N":
        print("Game Over")
        global start
        start = False
    elif q == "Y":
        pass
    else:
        print("try again")


def logic(p1, p2):
    # Rock
    if p1 == "Rock" and p2 == "Rock":
        print("tie")
    elif p1 == "Rock" and p2 == "Paper":
        print("Computer wins")
        score["computer"] += 1
    elif p1 == "Rock" and p2 == "Scissor":
        print("P1 wins")
        score["player"] += 1

    # Paper
    elif p1 == "Paper" and p2 == "Paper":
        print("tie")
    elif p1 == "Paper" and p2 == "Scissor":
        print("Computer wins")
        score["computer"] += 1
    elif p1 == "Paper" and p2 == "Rock":
        print("Player1 wins")
        score["player"] += 1

    # Scissor
    elif p1 == "Scissor" and p2 == "Scissor":
        print("tie")
    elif p1 == "Scissor" and p2 == "Paper":
        print("Player1 wins")
        score["player"] += 1
    elif p1 == "Scissor" and p2 == "Rock":
        print("Computer wins")
        score["computer"] += 1

    else:
        print("try again")


def game():
   
    scores()
    computer = random.choice(options)
    opt1 = input("Choose: \n0: Rock | 1: Paper | 2: Scissor")
   
    match opt1:
        case "0":
            player = "Rock"
            print(f"Player: {player} -  Computer: {computer}")
            logic(player, computer)
        case "1":
            player = "Paper"
            print(f"Player: {player} -  Computer: {computer}")
            logic(player, computer)
        case "2":
            player = "Scissor"
            print(f"Player: {player} -  Computer: {computer}")
            logic(player, computer)
        case _:
            print("invalid option, try again")



attemps = 0
while start:
    game()
