# Write a function called countVowels that takes in a string and returns the number of vowels in the string.


def countVowels(word):
    v = ["a", "e", "i", "o", "u"]
    res = 0
    for w in word:
        if w in v:
            res += 1
    print(res)


countVowels("javascript")
