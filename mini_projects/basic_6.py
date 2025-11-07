# Create a intermediate todo list

# Hints
# You might ask the user what to add
# You might use dictionaries to store the items and the qty
# Since this is a intermediate todo list, add the functionality to delete an item


shopping = {}

start = True

def deleteItem(shopping):
    while True:
        for item, qty in shopping.items():
            print(f"Item:{item} QTY:{qty}")

        item = input("what would you like to delete? Type NA to cancel")
        if item.upper() == "NA":
            return
        elif item in shopping:
            shopping.pop(item)
            print('Item deleted successfully')
        elif item not in shopping:
            print('No item in the shopping cart. Try again')

        elif item.upper() == "NA":
            return

def task():
    global start
    while True:
        item= input('what would you like to add?')
        qty=input('how many items?')

        shopping[item] = qty
        end = input('Do you want to continue? Y/N').upper()
        if end == 'N':
            print(shopping)
            q = input('This is your list, do you want to delete something? Y/N').upper()
            if q == "Y":
                deleteItem(shopping)
                return
            else:
                start = False
                print('goodbye!')
                return
        elif end == "Y":
            continue
        else:
            print('Invalid input... try again')


while start:
    task()
