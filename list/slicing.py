fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] 
print(all_fruits)# it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3] # it does not include the first index
print(orange_and_mango)
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(orange_and_lemon)