# Create a calculator function that accepts three params:

# Hint:
# two numbers to calculate and the operand

def calculator(a,b, operand):
    match operand:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case _:
            print('something wrong happened... try again')


calculator(7,7,"+")
        
