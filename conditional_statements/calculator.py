def calculator(num1, num2, operator):
    if operator == '+':
        sum = num1+num2
        return sum
    elif operator == '-':
        if num1 > num2:
            sum = num1-num2
            return sum
        elif num2 > num1:
            sum=num2-num1
            return sum
    elif operator == '*':
        sum = num1*num2
        return sum
    elif operator == '/':
        sum = num1/num2
        return sum
    elif operator == '%':
        sum = num1%num2
        return sum
    else:
        return "you have entered -ve value"

try:
    int1 = float(input("Enter num1: "))
    int2 = float(input("Enter num2: "))
    opr = input("Enter any operator out of these [+ , - , * , / , %]: ")

    calculated_value= calculator(int1, int2, opr)

    print(calculated_value)

except ValueError:
    print("enter valid number")
        