def check(year):
    if year %4==0:
        if year %100 != 0 and year % 400 ==0:
            return "leap year"
        else:
            return "not a leap year"
    else:
        return "not a leap year"




year = int(input("enter a year"))
leap = check(year)
print(f"the following year is {leap} ")