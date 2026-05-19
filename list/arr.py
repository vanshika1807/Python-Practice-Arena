lst = []
for i in range(0,8):
    lst.append(i)

print(lst)

user_input = int(input("Enter the range of your list: "))
list1=[]
for i in range(user_input):
    list1.append(int(input()))

print(list1[-2])