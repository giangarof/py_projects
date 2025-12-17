# check the vowels using a dictionary

def vowel_count(word):
    ls = ["a", "e", "i", "o", "u"]
    res = {}
    for w in word:
        if w in ls:
            # print(w)
            res[w] = res.get(w,0)+1
    return res

print(vowel_count("timeline"))