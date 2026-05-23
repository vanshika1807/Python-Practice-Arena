def calculate(radius):
    
    area_of_circle = round((3.14 * (radius**2)), 2)
    circumference = round((2 * 3.14 * radius),2)

    return f"The of circle is {area_of_circle} & The circumference of the circle is {circumference}" 

n1 = int(input("Enter the radius of circle: "))
print(calculate(n1))