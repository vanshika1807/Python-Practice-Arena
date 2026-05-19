seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days):
    return (f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}")  

# <--------User input in Python----->
#using input() to take user input

user_inut = input("Enter a value for the number of days to covert it in seconds\n")   #it is a input function

# Expression = an instruction that combines values and operators and always evaluates down to a single value
input = int(user_inut)
calculated_value = days_to_seconds(input)

print(calculated_value)

# now the problem with this code is that the input() fucntion will treat all the inputs as string or test not as a integer.abs
# so we will just now define user as int(user_input) this is nothing but casting - we will cast our user input into the int using python builtin function int()

