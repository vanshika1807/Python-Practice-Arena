age = int(input("Enter you age: "))
if(age>=18):
    print("You are old eugh to drive")
elif(age<18):
    rem_age = 18-age
    print(f"you need {rem_age} years to drive")