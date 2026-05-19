def leap_year(year):
    if year%400 ==0:
        return "Leap Year."
    elif year%100==0:
        return "Not a Leap Year."
    elif year%4==0:
        return "Leap Year."
    else:
        return "not a leap year"

try:
    int1 = int(input("Enter year: "))
    value = leap_year(int1)
    print(value)

except ValueError:
    print("enter valid number")
        