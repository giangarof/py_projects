# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# Simple math
# One years is 52 years (Don't pay attention to leap years for this case)

def life_in_weeks(age):

    age_in_weeks = age*52

    full = 90 * 52

    res= full - age_in_weeks

    print(f"You have {res} weeks left.")


life_in_weeks(56)
