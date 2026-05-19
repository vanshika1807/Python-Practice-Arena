'''
# What is list ?
- DT so far - String -> "Vanshika", float -> "6.7" , integrers -> 10, Boolean -> True or false
- To store multiple items in a single variables 
- A list can contain diff data types

'''

# but suppose I want my function to execute the same login repeatedly for multiple values - n such cases we would need a loop
# and then loop is call foor Loop

'''
# What is a for Loop?
- It is used for iterating over a sequence (like a list)
- so we can execute smth for each item in a list.
'''

seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days): 
    return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
    
def validate_and_execute():
    try:
    
        num = int(num_of_days)
        if num > 0:
            calculated_value = days_to_seconds(num)
            print(calculated_value)
        elif num == 0:
            print("you have entered 0")
        else:
            print("you entered -ve number, no conversion for you")
    
    except ValueError: #to cover any type of error we can leav it as 'except:' ----try/catch but here in python we have try/except
        print("you enter wrong value , dont ruin my  program.")


user_input = ""
while user_input != "exit":  #True --- boolean  || true --- just a string
    user_input = input("Enter a value for the number of days as coma separated list to covert it in seconds together: \n")  
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days in user_input.split(","): #a split() --> converts the string into a list
        validate_and_execute()

