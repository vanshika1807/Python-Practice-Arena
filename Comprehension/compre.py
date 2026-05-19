#dictionary/list/set comprehension

num = int(input())

#dict
sqr_dict = {x:x**2 for x in range(num)}
print(sqr_dict)

#list

sqr_list = [x**2 for x in range(num)]
print(sqr_list)

#set
sqr_set = {x**2 for x in range(num)}
print(sqr_set)

#tuple
sqr_tuple=tuple(x**2 for x in range(num))
print(sqr_tuple)