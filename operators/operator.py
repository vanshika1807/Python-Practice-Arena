#in python we have so many comparision operators
# -------------------------------
#  ==     Equal                   x==y
#  !=    Not Equal                x!=y
#   >  Greater than                x>y
#   <    Less Than                 x<y
#  >=  Greater than or equal to   x>=y
#  <=  Less then or equal to      x<=y
# -------------------------------

#in python we have so many arithemetic operators
# -------------------------------
#  +     Addition                  x+y
#  -     Subtraction               x-y
#  *     Multiplication            x*y
#  /     Division                  x/y
#  %     Modulus                   x%y
#  **    Exponentiation            x**y
#  //    Floor division            x//y
# -------------------------------

# All of them are used to compare 2 values

seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
    else : 
        return "you fool!!, enter a +ve number"

user_inut = input("Enter a value for the number of days to covert it in seconds\n")   

input = int(user_inut)
calculated_value = days_to_seconds(input)
print(calculated_value)

