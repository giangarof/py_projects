# return true if year is leap, otherwise return false


def year_leap(year):
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap=True
    else:
        is_leap = False


    print(is_leap)


year_leap(2020)
