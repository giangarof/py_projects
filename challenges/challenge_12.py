# Write a function called displayLikes that takes in an array of names and returns a string of who likes the post.

# The function should return a string formatted as follows:

# If no one likes it, it should return 'no one likes this'
# If one person likes it, it should return '{name} likes this'
# If two people like it, it should return '{name1} and {name2} like this'
# If three people like it, it should return '{name1}, {name2} and {name3} like this'
# If more than three people like it, it should return '{name1}, {name2} and {x} others like this'


def displayLikes(list):
    # if len(list) >= 1:
    #     if len(list) == 1:
    #         print(f"{list[0]} likes it")
    #     elif len(list) == 2:
    #         print(f"{list[0]} and {list[1]} likes it")
    #     elif len(list) == 3:
    #         print(f"{list[0]}, {list[1]} and {list[2]} likes it")
    #     else:
    #         print(f"{list[0]}, {list[1]} and {len(list) - 2 } more likes it")
    # else:
    #     print('no one likes it')

    match list:
        case []:
            print("No one likes it")
        case [a]:
            print(f"{list[0]} likes it")
        case [a,b]:
            print(f"{list[0]}, {list[1]} and {list[2]} likes it")
        case [a,b, *rest]:
            print(f"{list[0]}, {list[1]} and {len(list) - 2} more likes it")


displayLikes(['milo', 'mochi', 'ms kitty', 'dony', 'kiron', 'apollo'])
