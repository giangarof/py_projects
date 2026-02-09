# Write a function called isPalindrome that takes in a string and returns true if the string is a palindrome and false if it is not.

def isPalindrome(word):
    reversed = ''
    for w in word:
        reversed = w + reversed

    if reversed.lower() == word.lower():
        return True
    else:
        return False

print(isPalindrome("raceCar"))
