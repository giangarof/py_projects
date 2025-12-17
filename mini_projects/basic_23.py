# Write a function called find_factors which accepts a number and returns a list of all of the numbers which are is divisible 
# by starting from 1 and going up to the number.


def factors(nums):
    res = []
    for x in range(1, nums + 1):  # this line is self explanatory
        if (
            nums % x == 0
        ):  # if the number is divisible by the iteration then append it to the new list
            res.append(x)
    return res


print(factors(63636363999123))
