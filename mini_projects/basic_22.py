# Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string capitalized.

word = "this is awesome"


def myfunc(w):
    newWord = []
    newLs = w.split(" ")
    for x in newLs:
        cap = x[0].upper() + x[1::]
        newWord.append(cap)
    return " ".join(newWord)


print(myfunc(word))
