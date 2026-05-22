inp_str = "aaasssjhfhweuirwejfnsodhfweiohfjkaz"

for char in inp_str:
    print(char)
    if inp_str.count(char) ==1:
        print("char is: ", char)
        break