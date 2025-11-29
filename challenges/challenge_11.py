# In programming, "intersection" generally refers to finding the common elements between two or more collections of data, such as sets or lists.


# Write a function called arrayIntersection that takes in two arrays and returns an array containing the intersection of the two input arrays


def arrayInterseccion(list1,list2):
    inter=[]                        # empty array to store intersection
    for x in list1:                 # loop  over first list
        if x in list2:              # first condition: check if x in list2 
            if x not in inter:      # if x is not in inter[], append x
                inter.append(x)

    print(inter)                    # good practice to replace print for return

arrayInterseccion([1,2,4,5,3], [1,9,9,8,8,2,3])