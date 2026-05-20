#determine if the fruit is ripe, overipe or unripe based on it color.


fruit = input("Enter a fruit Name: ")
color = input("Enter the color of you fruit: ")

if fruit =="Banana":
    if color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    elif(color == "Green"):
        print("Unripe")
    else:
        print("if could be a chnage you enter a wrong fruit or either wrong color")
    
elif fruit=="Mango":
    if color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    elif(color == "Green"):
        print("Unripe")
    else:
        print("if could be a chnage you enter a wrong fruit or either wrong color")
elif fruit=="Apple":
    if color == "Red":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    elif(color == "Green"):
        print("could be a green apple")
    else:
        print("if could be a chnage you enter a wrong fruit or either wrong color")
else:
    print("Enter either from apple, mango , banana")