seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days): 
    return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
    
def validate_and_execute():
    try:
    
        num = int(user_input)
        if num > 0:
            calculated_value = days_to_seconds(num) #converted
            print(calculated_value)
        elif num == 0:
            print("you ghave entered 0")
        else:
            print("you entered -ve number, no conversion for you")
    
    except ValueError: #to cover any type of error we can leav it as 'except:' ----try/catch but here in python we have try/except
        print("you enter wrong value , dont ruin my program.")


user_input = input("Enter a value for the number of days to covert it in seconds\n")  
validate_and_execute()

#the above example is much easire than trying hundreds of if/else statements