# Create variables for your name, age, and city and print them.
name = 'Vanshika'
age = 24
city = 'Hyderbabd'
print(f"My name is {name} and I am {24} year old. I am based in{city} currently.")
print(" ")

# Write a program to swap two numbers.
print("USING 3 VARS")
num1 = 4
num2 = 6
print(f'Original Numbers : \n Num1 - {num1} \n Num2 - {num2}')
num3 = 0
num3 = num1
num1 = num2
num2 = num3
print(f"Numbers after Swapping : \n Num1 - {num1} \n Num2 - {num2}")
print(" ")
print("WITHOUT USING 3 VARS")
num4 = 5
num5 = 10
print(f'Original Numbers : \n Num1 - {num4} \n Num2 - {num5}')
num4 = num4 + num5
num5 = num4 - num5
num4 = num4 - num5 
print(f"Numbers after Swapping : \n Num1 - {num4} \n Num2 - {num5}")
print(" ")

#Take two numbers as input and print their sum.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter Num2: "))
Sum = num1 + num2
print("Sum of num1 & num2:",Sum)
print(" ")

#Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

print(" ")

#Create a list of 5 numbers and print the first and last element.
list1 = [1,4,6,8,2]
print(list1[0])
print(list1[-1])

#Add a new element to a list using append().
n = int(input("enter a number you want to append: "))
list1.append(n)
print(list1)
print(" ")

#Remove an element from a list using remove().
list1.remove(4) #removed only the first occurence of repeated value from left to right
print(list1)
print(" ")

#Create a tuple and print all elements using indexing.
t = (1,'Vanshika',85.5,True)
for i in range(len(t)):
    print(t[i])
print(" ")

#Write a program to count the number of elements in a list.
print(f"Toral number of elements: {len(list1)}") #short cut
count=0 #manual way
for i in list1:
    count +=1
print(count)

#Write a program to find the largest number in a list.

print(max(list1)) #short cut
largest = 0 # manual way
for i in list1:
    if i>largest:
        largest = i
print("The largest number is: ", largest)
print(" ")

#Create two sets and find their union.
set1 = {1,2,3,4,5}
print(set1)
set2 = {2,3,7,8,10}
print(set2)
union = set1 | set2
#aunion1 = set1.union(set2)
print(f"the union of two declared sets is: ", union)
#Find common elements between two sets.
common = set1 & set2
print("the common / intersection of two sets: ", common)
print(" ")

#Create a dictionary with student name and marks.
student= {
    'Vanshika' : 85,
    'John' : 67,
    'Maria': 45,
    'Sam': 56
}

print(student.items())

#Update a value in a dictionary.

student['Vanshika'] = 90
print(student)

#Check whether a key exists in a dictionary.
if 'Sam' in student:
    print("key exists")
else:
    print("Does not exits")
print(" ")

#Write a program to reverse a string.
str1 = "Hello I am learning Python"
reverse = ''
for char in str1:
    reverse = char + reverse

print(reverse)
print(" ")

#Write a program to count vowels in a string.
count = 0
for char in str1:
    if char in 'AEIOUaeiou':
        count+=1

print(count)
print(" ")

#Convert a string into uppercase and lowercase.
print(str1.lower())
print(str1.upper())

#Write a program to check whether a string is palindrome
string1 = input("enter a string1: ")

reverse = ''
for char in string1:
    reverse = char + reverse

if reverse.lower() == string1.lower():
    print("palindrome!")
else:
    print("not palindrome!")

print(" ")

#Write a program to count frequency of characters in a string.
