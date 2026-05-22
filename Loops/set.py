fruit = ['banana', 'orange', 'mango', 'lemon', 'lemon', 'banana']

unique_item=set()

for i in fruit:
    if i in unique_item:
        print("Duplicate: ", i)
    unique_item.add(i)