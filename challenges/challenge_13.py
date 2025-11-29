# Find the missing number from a list
# Example 1,2,4,5

# Hint 1
# Keep in mind that the index start at 0
# Keep in mind that the index of 1,2,4,5 is not the same of 1,2,3,4,5
# Keep in mind you must substact the result from expected number and the actual sum

# Hint 2
# Keep in mind you're adding the index value, not adding the index itself


def findMissingNumber(list):

    actualSum = sum(list)
    expectedSum = 0

    for x in range (min(list), max(list) + 1 ):
        expectedSum += x
        # print(x)

    misssingNumber = expectedSum - actualSum 

    print(misssingNumber)

findMissingNumber([10,11,13,14,15])
