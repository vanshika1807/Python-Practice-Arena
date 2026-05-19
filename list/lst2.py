hours = 24 * 60 
name_of_unit = "Hours"
def calculate_hours_in_days(num):
    return f"{num} days are : {num * hours} {name_of_unit}"


value = int(input("Enter a number that you want to convert into hours: "))

print(calculate_hours_in_days(value))

