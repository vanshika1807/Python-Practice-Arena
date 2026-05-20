'''
determine if a year is a leap year
--> should be divible by 400
'''



def check_year(year):
    num = int(year)
    if (num%400 == 0) or (num%4==0 and num%100!=0) :
        return f"{num} is leap year."
    else:
        return f"{num} is not a leap year."


try:
    year = input("Enter a Year: ")
    print(check_year(year))
except ValueError as e:
    print("Oops soemthing is wrong as there is a ", e)
