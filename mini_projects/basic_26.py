# create a todo list using dictionary


myTodo = {}


def myFunc():
    while True:
        task = input("Add task: ")
        level = input(
            "How important is this task? 1:Must be done before the end of the day | 2:Can wait 2-3 days | 3:Must be done asap"
        )
        myTodo.update({task:level})

        if len(myTodo) % 3 == 0:
            ask = input("Do you want to add more? Y/N").lower()
            if ask == "n":
                print("Your TODO list (using dictionary)")
                print(myTodo)
                break
        print(myTodo)


myFunc()
