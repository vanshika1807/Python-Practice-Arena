def sq_num(*num1):
    sq_list=[]
    for i in num1:
        sq = i**2
        sq_list.append(sq)
    return sq_list

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))
f = int(input("Enter a number: "))
g = int(input("Enter a number: "))
result=sq_num(a,b,c,d,e,f,g)
print(result)
