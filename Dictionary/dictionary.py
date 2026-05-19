chai_types= {'Masala': 'Spicy', 'Ginger':'Zesty', 'Green':'Fresh'}

print(chai_types.items())

for i in chai_types:
    print(i +" -> "+ chai_types[i])

for i in chai_types:
    if "Masala" in chai_types:
        print("that will be 50")
    else: 
        print("is free for testing")

for k, v in chai_types.items():
    print(k, v)