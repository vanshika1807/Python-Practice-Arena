# Declare an empty list

list1 = list()
print(list1)

list2 = []
print(list2)

# Declare a list with more than 5 items
list3 = [1, 2, 3,4,5]

# Find the length of your list
print(len(list3))

# Get the first item, the middle item and the last item of the list
first = list3[0]
last= list3[-1]
middle=list3[len(list3) // 2]
print( f"First:  {first}  Last: {last} Middle: {middle}")

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Vanshika", 24, 5.2, "Single", "Hyderabad - 500032"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first = it_companies[0]
last= it_companies[-1]
middle= it_companies[len(list3) // 2]
print( f"First:  {first}  Last: {last} Middle: {middle}")

# Print the list after modifying one of the companies
print("Original List: " , it_companies)

it_companies[3] = "Cognizant"

print("New List: ",it_companies)

# Add an IT company to it_companies
it_companies.append("Berkadia")
print("Appened new Comp: ",it_companies)

# Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Alphabet")
print("Inserted New Comp in a List: ",it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
str1 = it_companies[0]
print(str1.upper())

# Join the it_companies with a string '#;  '
separator = '#;  '
joined_companies = separator.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list.
does_exit = "Facebook" in it_companies
print(does_exit)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)


# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
sliced=it_companies[0:3]
print(sliced)

# Slice out the last 3 companies from the list
sliced=it_companies[-3:]
print(sliced)

# Slice out the middle IT company or companies from the list
length = len(it_companies)
mid = length // 2
middle_one = it_companies[mid:mid+1]