# what if a user enters a wrong value - we do not want our program to crash

seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds(number_of_days):
    conditional_check = number_of_days>0 # printing boolean values - Tru or False --- Boolean Type of Data
    print(type(conditional_check)) #will returnt he data-type of conditional check ---> type is a function 
    if number_of_days > 0:   #this segment right here we are doing a check called conditional - if correct then do something otherwise do something else ; the condition  can be true or false ---> these T and F are represented by there own value ---> called boolean values (True or False)
        return f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}"
    elif number_of_days == 0:  # '=' is used to assign a value & '==' is for comparasion
        return "you entered a 0, please enter a valid positive number"
    else : 
        return "you entered a negative value. So, no conversion for you!!!!"
# <--------User input in Python----->
#using input() to take user input

user_inut = input("Enter a value for the number of days to covert it in seconds\n")   #it is a input function

# Expression = an instruction that combines values and operators and always evaluates down to a single value

calculated_value = days_to_seconds(int(user_inut)) # int function expect some value; it can convert float to int

print(calculated_value)

#here, we got string data type ---> we convert it into int --> pass it on to our function ----> evalutes if--->negative returns other string

# with this program there is an issue like if a user enters a wrong value - then our program will blow , it will crash it will not work at all 
#we will need something to endle those error like if a user enter a float or string value as an input the program will return a ValueError so 
#we need something that can handle that issue before inpur even goes to our function for calculatetion
#in such cases Error handling comes into the picture.
#another way is also using if else only.