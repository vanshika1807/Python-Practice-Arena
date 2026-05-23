def poly(para1, para2):
    return para1*para2
     

a = input("Enter a parameter1: ")
b = input("Enter parameter2: ")
if a.isdigit():
    a = int(a)

if b.isdigit():
    b = int(b)


print(poly(a,b))