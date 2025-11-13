# FizzBuzz

# Instructions

# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

nums = range(1,101)

for n in nums:
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 5==0:
        print('Buzz')
    elif n % 3==0:
        print('Fizz')
    else:
        print(n)
