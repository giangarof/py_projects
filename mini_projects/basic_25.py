# create a todo list using list


myTodo = []
def myFunc():
    while True:
        ask = input("Add task: ")
        myTodo.append(ask)
        
        if len(myTodo) % 3 == 0:
            ask = input('Do you want to add more? Y/N').lower()
            if ask == 'n':
                print('Your TODO list (using list)')
                print(myTodo)
                break
        print(ask)

    

myFunc()