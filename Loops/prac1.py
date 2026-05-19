#easliest way to declare list in python is lst

fruits =['apple','mango','orange']
numbers = [1,2,3,4,5,6,7,8,9]
sum1=0
sum2=0
for i in numbers:
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i

print(sum1) 
print(sum2) 