order = input("Enter the coffe size: ").lower()
extra_shots = order == "medium" or order == "large"
if order =="small":
    coffee = "Your ordered: " + order + " & here is your coffee"

elif order =="medium":
    coffee = "Your ordered: " + order + " & here is your coffee" 

elif order =="large":
     coffee = "Your ordered: " + order + " & here is your coffee"

else:
     coffee= "something went wrong"

if extra_shots:
    print("Congrats you got extra shots")

print(coffee)