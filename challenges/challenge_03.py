# Write a function called calculator that takes in 2 numbers and an operator and returns the result of the calculation.

def calculator(a,b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "/":
            return a / b
        case "*":
            return a * b
        case _:
            return "Invalid operator, try again"
        

print(calculator(5,5,"/"))