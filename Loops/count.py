numbers = [1,-2,4,90, -6, 0 , -5 , -8, 6 ,-6, -4, -8, -7 , 6 , 4 , 7 , 2 , 4, 3]

positive_number_count=0
negative_number_count = 0
zero_count=0

for i in numbers:
    if i>0:
        positive_number_count +=1
    elif i == 0:
        zero_count+=1
    else:
        negative_number_count +=1

print("Total +ve: ", positive_number_count, "| Total -ve: ", negative_number_count , "| Total 0 present: ", zero_count)
