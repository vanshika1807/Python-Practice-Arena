n = int(input("Enter a number whose table you want to print: "))
range_n = int(input("Enter the number till when you wantto tprint the table: "))

for i in range(1, range_n+1):
    if i==5:
        continue
    print(f"{n} x  {i} = {n*i}")
    

