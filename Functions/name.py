def generate_name(first_name, last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name

str1 = input("Enter a first nane: ")
str2 = input("Enter your last name: ")
print(generate_name(last_name=str2, first_name=str1))