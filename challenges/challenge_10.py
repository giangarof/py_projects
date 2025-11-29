# Write a function called removeDuplicates that takes in an array and returns a new array with duplicates removed.



def removeDuplicates(list):
    newList = []
    for ls in list:
        # print(ls)         #Print all the elements from the list
        if ls in newList:   # check if element is in the list
            pass 
        else:               # if is not in the list, the element is added
            newList.append(ls)
    print(newList)

removeDuplicates([1,2,1,1,1,2,3,3,4,5])