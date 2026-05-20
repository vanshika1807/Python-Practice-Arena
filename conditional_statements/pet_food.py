# pet_value = {}

# n = int(input("Enter the number of pets you want to check: "))

# for i in range(n):
#     pet, age = input("Enter the species & age of your pet: ").split()
#     pet_value[pet] = age

# print("Your Pets Details: ", pet_value)

# print("Food Recommendations: ")

# for pet in pet_value:
#     if pet.lower() =="dog":
#         print("")


pet = input("Enter the dog species: ").lower()
age = int(input("Enter the age of you dog: "))

if pet=='dog' and age<2:
    print("Puppy Food")
elif pet=='cat' and age>5:
    print("Senior Cat food")
else:
    print("no pet")
