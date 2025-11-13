# From basic_2.py
# Recreate the calculator app using:
# 1. ask the user the numbers to calculate
# 2. ask the user which operand to use


def calculator():
    num1 = int(input("first number?\n"))
    num2 = int(input("second number?\n"))
    operand = input("which operand?: + | - | / | *\n")

    match operand:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case _:
            print("something wrong happened... try again")


calculator()