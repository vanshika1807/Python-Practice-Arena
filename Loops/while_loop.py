#what if we wants our Application for another value or some values simutaneously till the condition is not satisfied
#we can achieve that using while
#we want our program to keep running
#Looping --> to execute logic multiple times & python have 2 types of loop commands
#how many that logic should get executed is stated in the condition of that loop
#condition can be like - until 10 times or until certain condition happens
#condtions ----> evaluates to true or false & are most  commonly used in "if statements" and "loops"
#condition is checking some login & it return either true or false

#----------------------------

# what are while loop?
'''
In while loop, execute a set of statements as long as a condition is true.
'''
#-------------------------------
seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days): 
    return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
    
def validate_and_execute():
    try:
    
        num = int(user_input)
        if num > 0:
            calculated_value = days_to_seconds(num)
            print(calculated_value)
        elif num == 0:
            print("you ghave entered 0")
        else:
            print("you entered -ve number, no conversion for you")
    
    except ValueError: #to cover any type of error we can leav it as 'except:' ----try/catch but here in python we have try/except
        print("you enter wrong value , dont ruin my program.")


user_input = ""
while user_input != "exit":  #True --- boolean  || true --- just a string
    user_input = input("Enter a value for the number of days to covert it in seconds\n")  
    validate_and_execute()

