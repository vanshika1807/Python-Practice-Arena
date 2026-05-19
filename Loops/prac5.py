num1 = int(input("enter a number: "))

for i in range(num1):
    for c in range(num1-i):
        print("*", end="")
    print()