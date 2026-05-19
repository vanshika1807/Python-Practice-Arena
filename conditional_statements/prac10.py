def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['March','April','May']:
        return 'Spring'
    elif month in ['June','July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month name. Please enter a full, valid month name.'

try:
    user_input = input("Enter a month name: ")
    month_entered_by_user = check_season(user_input)
    print(f"{user_input} is a {month_entered_by_user} season month.")

except ValueError:
    print("Enter a month name only.")