#what is we want is to avoid these duplation of code in variables.py file

#in order to do that we can do these by using functions - we dont want to write is gaian and again

# function - to avoid repating the same login

#how to do we create function - we do that by using a def "keyword"

#if I amnot calling the fucntion anywhere - it will not work at all

#so inorder to make my function work I need to call it somewhere okayy!!


seconds = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_seconds():
    print(f"100 days are {100 * seconds} {name_of_unit}") #here indentation plays an importat role --- I eman this one line belongs to the function "days_to_seconds" , now this function contsists of only one line but it can consists of several lines
    print("all good!!!")#currenty is nothing but we have hard coded the values now
    print("I will succeeed one day for sure")

days_to_seconds() # here only I am actually calling the function - these two round craces - nothing but an indication of calling
    
#--------------function parameter----------------

# now this above code will work for the logic for 100 days - what if I want it for more days - here function parameter will come into the picture

#we can achieve that giving our function some inpur values - which are called input parameters

# function parameters --> information can be passed into functions as parameteres & parameters are also called arguments

# days_to_seconds(35) --somewhat like this I can acheive that but first we need to make our function work in a way to accept those value

# we can achieve that by making that function accept the input by using a variables

def days_to_seconds(number_of_days):
    print(f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}")  

days_to_seconds(1)
# in function above  we have defined a variable to take the number of days as an argument/parameter "number_of_days" and then the calling of function line is actually accepting "56" & givign the output



#multiple input parameter
def days_to_seconds(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * seconds} {name_of_unit}")  
    print(custom_message)

days_to_seconds(1,"Henlonoooooo")

#variables scopes in function

#scope = variable scope means where is avirable that function uses is defined
#if defined out side the function have global scopes
#if defined within that function have locals cope because they are defines inside the function

print("------testing scope-------------")

def scope_check(number_of_days):
    my_var = "Variable inside function"
    print(name_of_unit) # will print as called global variable
    print(number_of_days) #will gonna return an error as it is local variable of "days_to_seconds" function
    print(my_var)

scope_check(56)


