def check_score(score):
    if score <0 or score > 100:
        return "Score should be between the range of 0-100"
    elif score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
try:
    user_input = float(input("Enter you Score :"))
    if user_input.is_integer():
        calculated_value = check_score(user_input)
        print(calculated_value)
    else:
        print("please enter a whole number.")

except ValueError:
    print("Please enter a valid number")


