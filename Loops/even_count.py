numbers=[]
even_count=0
odd_count=0

try: 
    n = int(input("enter the range of number: "))
    for i in range(1, n+1):
        num = int(input('Enter the number Now: '))
        numbers.append(num)

    for num in numbers:
        if num%2==0:
            even_count += 1
        else:
            odd_count +=1
    
    print(f"Total Even Count: {even_count} \nTotal odd Count: {odd_count}")

except ValueError:
    print("Something went wrong")    


