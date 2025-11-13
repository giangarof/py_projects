def compatibility(name1, name2):
    name_store1 = 0
    name_store2 = 0

    word1 = "true"
    word2 = "love"

    for n in name1.lower():
        for w in word1:
            if w == n:
                name_store1 += 1

    for n in name2.lower():
        for w in word1:
            if w == n:
                name_store1 += 1

    for n in name1.lower():
        for w in word2:
            if w == n:
                name_store2 += 1

    for n in name2.lower():
        for w in word2:
            if w == n:
                name_store2 += 1

    res = name_store1 * 10 + name_store2
    print(res)


compatibility("Orfeo", "Euridice")
