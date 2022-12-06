def find_the_day(user_day,user_month,user_year):
    
    year_end = user_year[-2:]
    year_end = int(year_end)

    leap_year = int(year_end) % 4
    quotient = int(year_end / 4)

    date = int(user_day)
    month = int(user_month)
    year = int(user_year)

    if leap_year == 0:
        if month == 1:
            month_code = 6
        elif month == 2:
            month_code = 2
    else:
        if month == 1:
            month_code = 0
        elif month == 2:
            month_code = 3


    if month == 3:
        month_code = 3
    elif month == 4:
        month_code = 6
    elif month == 5:
        month_code = 1
    elif month == 6:
        month_code = 4
    elif month == 7:
        month_code = 6
    elif month == 8:
        month_code = 2
    elif month == 9:
        month_code = 9
    elif month == 10:
        month_code = 0
    elif month == 11:
        month_code = 3
    elif month == 12:
        month_code = 5

    if year>=1600 and year<=1699:
        year_code=6
    elif year>=1700 and year<=1799:
        year_code=4
    elif year>=1800 and year<=1899:
        year_code=2
    elif year>=1900 and year<=1999:
        year_code=0
    elif year>=2000 and year<=2099:
        year_code=6

    total = year_end + quotient + date + month_code + year_code
    day = total % 7

    if day==0:
        return "Sunday"
    elif day==1:
        return "Monday"
    elif day==2:
        return "Tuesday"
    elif day==3:
        return "Wednesday"
    elif day==4:
        return "Thursday"
    elif day==5:
        return "Friday"
    elif day==6:
        return "Saturday"