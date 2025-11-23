# BlackJack game
import random

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


# generates a random dictonary
def draw_card():
    key, value = random.choice(list(cards.items()))
    return {key: value}


# display the hands card & the total
def display(p1, p2):
    print(f"Your hand: {p1} Total: {hand_total(p1)}")
    # print(f"Computer hand: {p2}")
    # print(f"Your total: {hand_total(p1)}")
    # print(f"computer total: {hand_total(p2)}")


# calculate the total value
def hand_total(cards):
    total = 0
    # print("here", cards)
    for card in cards:
        for k, v in card.items():
            # print(k,v)
            total += v

    return total


# start the game
def game():
    print("*****")
    print("BlackJack Game")
    print("*****")

    # player1
    player1 = [draw_card(), draw_card()]  # add the main 2 cards
    computer = [draw_card(), draw_card()]  # add the main 2 cards

    while True:
        display(player1, computer)

        # ask if main player wants another card
        ask = input("Do you want to grab another card? y/n")

        if ask != "y":
            # print(hand_total(player1))
            # print(hand_total(computer))
            break
        else:
            player1.append(draw_card())

            if hand_total(computer) < 19:
                computer.append(draw_card())
                print('computer draw a card...')

    p1 = hand_total(player1)
    p2 = hand_total(computer)

    if p1 > 21:
        print("You bust! Dealer wins!")
    elif p2 > 21:
        print("Dealer busts! You win!")
    elif p1 > p2:
        print("You win!")
    elif p1 < p2:
        print("Dealer wins!")
    else:
        print("It's a tie!")

    print(f"Your total: {p1}")
    print(f"computer total: {p2}")


game()
