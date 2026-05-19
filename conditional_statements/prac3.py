print("I am and 25 year old.")
age1= input("Enter your age: ")
try:
    age=float(age1)
    if(age>0):
        if(age==25):
            print("wow me & u are of same age")
        elif(age>25 and age<90):
            age_diff=age-25
            print(f"u are {age_diff} older than me.")
        elif(age>90 and age<100):
            print(f"you are old man.Are u alright how are you acessing th einternet if you body alright")
        elif(age<25):
            age_diff=25-age
            print(f"u are {age_diff} younger than me.")
        else:
            print(f"hoe are you living man?")
    else:
        print("age cannot be -ve")
except ValueError:
    print("dont ruin my program")