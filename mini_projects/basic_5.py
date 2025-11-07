# Create a very basic todo list

# Hints
# You might ask the user what to add
# You might use list to store the items

shoppingList = []
start = True

def addmore():
    global start
    while True:
        q = input("Do you want to add something else? Y/N").upper()
        if q == "Y":
            return
        elif q == "N":
            print(shoppingList)
            start = False
            return
        else:
            print("try again... Y/N")


while start:
    q = input('what do you want to add')

    shoppingList.append(q)

    addmore()



