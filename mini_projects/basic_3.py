# Create a tip calculator

# Instructions

# Ask for the total bill
# Ask how much tip would you like to give: 10%, 12%, 15%, or something different but greater than 0
# Ask how many people are splitting the bill
# Output how much each person must pay (keep in mind that when you're paying usually is in float format)

# Tips
# Keep in mind you must calculate the percentage and add it to the total bill
# Keep in mind you must divide the total with the people that will pay

# Solution

total_bill = float(input("How much is the total bill? "))
print(f'${total_bill}')
tips = int(input('How much tip would you like to give? '))
print(f'{tips}%')

split_in = int(input('How many people are spliting the bill?'))
print(split_in)

def calculation(tip, total, split):
    total_before_tip = (tip/100) * total
    total_after_tip = total_before_tip + total
    total_after_split = total_after_tip / split
    print(total_after_split)

calculation(tips,total_bill,split_in)