seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days): 
    return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
  
def validate_and_execute():
    if user_input.isdigit():
        num = int(user_input)
        if num > 0:   
            calculated_value = days_to_seconds(num)
            print(calculated_value)
        elif num == 0:  
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you enterend a -ve value")
        
        
    else:
        print("you enter wrong value , dont ruin my program.")



user_input = input("Enter a value for the number of days to covert it in seconds\n")  
validate_and_execute()

#these if - else are very messy - we should not go to this level 