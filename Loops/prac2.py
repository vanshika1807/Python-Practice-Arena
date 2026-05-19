num = int(input("Enter a number: "))
i=0
sum1=0
sum2=0
while(i<=num):
    if(i%2==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
    i=i+1

print(sum1, sum2)
