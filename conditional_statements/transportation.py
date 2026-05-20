num = input("Enter the distance you are travelling in kms: ")

try: 
    distance = float(num)
    activity = "nothing" if distance == 0.0 else "travel"
    print(activity)

    if( distance < 3):
        print("you should walk")

    elif(distance >= 3 and  distance <= 15):
        print("Take Bike")

    elif(distance > 15):
        print("Take Car")

    else:
        print("wrong input")
except ValueError:
    print("please enter the distance in num")

finally:
    print("Execution completed!")
