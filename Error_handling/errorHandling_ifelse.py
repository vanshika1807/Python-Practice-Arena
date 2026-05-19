seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days):
    conditional_check = number_of_days>0 
    print(type(conditional_check))  
    if number_of_days > 0:   
        return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
    elif number_of_days == 0:  
        return "you entered a 0, please enter a valid positive number"
  #we dont usualy need else condition is not necessary in Python
  #as a clean we shoudl always put logics inside a function.

def validate_and_execute():
    if user_input.isdigit():
        num = int(user_input)
        calculated_value = days_to_seconds(num)
        print(calculated_value)
    else:
        print("you enter wrong value , dont ruin my program.")



user_input = input("Enter a value for the number of days to covert it in seconds\n")  
validate_and_execute()
