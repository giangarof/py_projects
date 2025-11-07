# Write a function called findMaxNumber that takes in an array of numbers and returns the largest number in the array.

nums = [1,20,2,99,3,4,5]
def findMaxNumber(num):
    largest= 0
    for n in num:
        if n > largest:
            largest = n
    print(largest)

findMaxNumber(nums)