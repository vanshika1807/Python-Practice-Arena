'''
# what are sets:
- let take an exmaple - in my list I can have sme duplicate value -
another built-in data type in python
- does NOT allow duplicate value
#where to use it?
- when we dont want indexing 
- O(1)
'''

Months = ["January", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(set(Months))
print(Months)
print(type(set(Months)))
print(type(Months))

my_set= {"Jan", "Feb", "Mar", "Mar" , "Jan"}
# print(my_set[1]) ---> this like will error out because 
'''
Set are Unordered & Unchangeable
    Items in a set do no have a defines order!
    Items cannot be reffered to by index
    Items cannot be changed, only added/removed
    can be iterated using for loop
'''
my_set.add("Apr")
print(my_set)
my_set.remove("Mar")
print(my_set)
Months.remove("January")
print(Months)

