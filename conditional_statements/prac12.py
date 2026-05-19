def compare_number(num1, num2):
    if num1<num2:
        return f"{num1} is less than {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    else:
        return f"a is equal to b."

try:
    user_input1 = float(input("Enter Num1: "))
    user_input2 = float(input("Enter Num2: "))

  
    calculated_value = compare_number(user_input1, user_input2)
    print(calculated_value)
  
        
except ValueError:
    print("Please enter a whole number")


