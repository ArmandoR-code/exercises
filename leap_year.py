# This program tells you if the current year it's leap or not
import datetime

year = datetime.datetime.today().year
not_leap = "is not a leap year"
leap = "is a leap year"

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, not_leap)
        else:
            print(year, leap)
    else:
        print(year, leap)
else: 
    print(year, not_leap)
 