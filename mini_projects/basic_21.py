# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.

def multiply_even(ls):
    newlist = []        # new list to store the even numbers
    product = 1         # every number multiplied by 1 returns the number itself

    for l in ls:
        if l % 2 == 0:
            newlist.append(l)

    for i in newlist:
        product *= i

    return product


print(multiply_even([2, 3, 4, 5, 6]))
