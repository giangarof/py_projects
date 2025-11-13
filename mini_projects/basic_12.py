# Bid game


start = True

bidders = {}


def calculate_the_highest(bid):
    global start
    highest = 0
    res = {}
    for k, v in bid.items():
        # This code checks for the highest
        if v > highest:
            highest =v
            res = {k: v}
        # This code checks for a tie
        elif v == highest:
            print("There is a Tie beetween the bidders! Please start the offert again")
            start = False
            return
    
    for name, ammount in res.items():

        print(f"Winner is {name} with {ammount}")  


def bid():
    print("******")
    print("Bid Game")
    print("******")
    global start

    while True:
        if len(bidders) >= 2:
            ask = input("They are more bidders?").lower()
            if ask == "y":
                name = input("Who is the next bidder?")
                num = int(input("How much do you want to bid?"))
                bidders[name] = num
            elif ask == "n":
                calculate_the_highest(bidders)

                start = False
                return
            else:
                print("invalid input, try again y/n")

        elif len(bidders) == 0:
            name = input("Who is the first bidder?")
            num = int(input("How much do you want to bid?"))
            bidders[name] = num
        else:
            name = input("Who is the next bidder?")
            num = int(input("How much do you want to bid?"))
            bidders[name] = num


while start:
    bid()
