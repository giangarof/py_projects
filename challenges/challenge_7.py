# Write a function called reverseString that takes in a string and returns the reverse of that string.
# The idea is not to use built-in methods

def reverseString(word):

    # first way: Slicing
    # return word[::-1].lower()

    # Second: Loop
    res = '' # a new variable to store the reversed word
    for w in word.lower():  # Loop over the sting
        res = w + res   # Append each character to the res variable: 
                        # w + res meaning:
                        # Adding the character to the existing result
    return(res)


print(reverseString('heLLo'))
