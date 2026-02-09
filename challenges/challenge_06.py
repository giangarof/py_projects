# Write a function called titleCase that takes in a string and returns the string with the first letter of each word capitalized.


def titleCase(w):
    word = w.lower().split(' ') # here: it does lower case the word and split each word saving it into a list
    l = [] # empty list lo lated attach the result
    for x in word: # loop over the string
        wd = x[0].upper() + x[1:] #upper case the first letter and slice the rest
        l.append(wd) # append to the empty list
    word = " ".join(l) # join the strings 
    return word

    # another solution more easy

    # update = w[0].upper() + w[1:]
    # return update


print(titleCase("heLlo worLd"))
