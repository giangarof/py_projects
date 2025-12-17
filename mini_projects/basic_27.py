# Write a function called includes which accepts a collection, a value, and an optional starting index. 
# The function should return True if the value exists in the collection when we search starting from the starting index. 
# Otherwise, it should return False.


def includes(collection, search, start=0):

    if start == 0:

        if isinstance(collection, list):
            if search not in collection:
                return False
            else:
                return True
        elif isinstance(collection, str):
            ls = list(collection)
            print(ls)
            if search not in ls:
                return False
            else:
                return True

        elif isinstance(collection, dict):
            if search not in collection.values():
                return False
            else:
                return True

    else:
        # start looking by the index
        searchByIndex = collection[start:]
        # print(searchByIndex)
        # print(search)
        if isinstance(collection, list):
            if search not in searchByIndex:
                return False
            else:
                return True
        elif isinstance(collection, str):
            ls = list(collection)
            if search not in ls:
                return False
            else:
                return True


# print(includes([1, 2, 3], 1))  # True
# print(includes([1, 2, 3], 1, 2))  # False
# print(includes({"a": 1, "b": 2}, 1))  # True
# print(includes({"a": 1, "b": 2}, "a"))  # False
# print(includes("abcd", "b"))  # True
# print(includes("abcd", "e"))  # False
