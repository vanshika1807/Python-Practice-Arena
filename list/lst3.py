def calculate_value(days):
    return f"{days} are {5*days}"


user_input = int(input("Enter the input as coma separated lsit: "))
for num in user_input:
    print(calculate_value(num))