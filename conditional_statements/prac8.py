def check_if_you_can_drive_or_not(age):
    if age >= 18:
        return("You are old enough to learn to drive.")

    else:
        rem_year = 18 - age
        return(f"You need {rem_year} more years to learn to drive.")
  
try:  
    num = float(input("Enter your age: "))

    if num.is_integer():
        user_input = int(num)
        if num<0:
            print("Age cannot be negative")
        else:
            calculcate_age = check_if_you_can_drive_or_not(user_input)
            print(calculcate_age)
    else:
        print("Age should be a whole number")

except ValueError:
    print("Enter a Valid Value")
