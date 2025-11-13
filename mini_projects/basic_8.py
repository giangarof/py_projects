# Hangman

# This project is more like an intermediate level due for the logic and workflow

# Hints:
# You will need to use functions ans loops. Conditional statements as well
# The word to guess must replace each character with _
# The user need to guess the wight word, either by guessing the whole word or character by character
# If the user guess wrong, a life is taken
# One important part is to replace the _ with the actual letter, you might use enumarate()
#

start = True
secret = 'galaxy'
display = ["_" for _ in secret]  # Display the secret word being build
store = []  # Store the guessed words
lifes = 6

def logic(char, display, secret):

    for i,w in enumerate(secret):
        if char == w:
            display[i] = char


def game():
    global start
    global secret
    global display
    global lifes

    if lifes == 0:
        print("game over")
        start = False
    else:
        print("current lives: ", lifes)
        if "".join(display) == secret:
            print('You have won')
            start = False

        else:
            ask = input("guess the word\n")
            if ask == secret:
                print("You've guessed the right word. Congratulations!")
                start = False
            elif ask in secret:
                logic(ask, display, secret)
                print(" ".join(display))
            else:
                lifes -= 1


while start:
    game()
