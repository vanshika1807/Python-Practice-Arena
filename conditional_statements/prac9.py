def check_even_odd(number):
    if number % 2 == 0:
        return f"the {number} you have entered is even."
    else :
        return f"the {number} you have entered is odd"

user_input = input("enter a number ")

num = int(user_input)

calculated_value = check_even_odd(num)

print(calculated_value)

