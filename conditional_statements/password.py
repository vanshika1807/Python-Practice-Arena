'''
Check if the password is "Weak", "Medium", or "Strong".
Criteria:
<6 chars (weak)
6-10 chars (Medium)
>10 chars (Strong)
'''
# simple
'''
password = input("Enter your password: ")

if password == " ":
    print("password cannot be null")
else:
    if(len(password) < 6):
        act = "Weak Password"
    elif(6 <= len(password)<=10):
        act = "Medium"
    else: 
        act = "Strong"
    
    print(act)
'''
# advanced

import getpass

password = getpass.getpass("Enter your password: ")

if password == "":
    print("password cannot be null")
else:
    if(len(password) < 6):
        act = "Weak Password"
    elif(6 <= len(password)<=10):
        act = "Medium"
    else: 
        act = "Strong"
    
    print(act)


