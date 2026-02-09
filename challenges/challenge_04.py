# Write a function called countOccurrences() that takes in a string and a character and returns the number of occurrences of that character in the string.


def countOccurrences(character, string):
    occurrences = 0
    for s in string:
        if character == s:
            occurrences += 1
    
    return occurrences

countOccurrences("l", "hello world")
