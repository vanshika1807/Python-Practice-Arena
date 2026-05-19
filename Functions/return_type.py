# return value = A function can return data as a result
# we can instead of printing we can return the value

seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days):
    return print(f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}")  

my_var= days_to_seconds(4)
print(my_var)