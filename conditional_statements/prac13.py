def compare_with_my_age(number):
    if number == 25.0:
        return f"You & me are of same age. I am also {number}."
    elif number > 25:
        age_diff = number-25
        if age_diff==1:
            return f"You are {age_diff} year older than me."

        else:
            return f"You are {age_diff} years older than me."
    else:
        age_diff = 25 - number
        if age_diff==1:
            return f"Awwwww!!!!! You are {age_diff} year younger than me."
        else:
            return f"Awwwww!!!!! You are {age_diff} years younger than me."

try:
    user_input = float(input("Enter your age: "))
    if user_input < 0:
        print("Hey! Age can't be negative man!")

    else:
        calculated_value = compare_with_my_age(user_input)
        print(calculated_value)

except ValueError:
    print("Please enter a whole number")
