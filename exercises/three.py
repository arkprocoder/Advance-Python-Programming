'''

3. Write a python program to find the area of square, rectangle and circle. Print the results. 
Take input from user

'''

# Area of circle = pi*r*r
# square = a*a
# rectangle = l*b



import math

r=int(input("Enter the radius of a circle : \n"))
print("Area of a circle is :", math.pi*r*r)

a=int(input("Enter the side of a Square : \n"))
print("Area of a Square is ",a*a)

l=int(input("Enter the length : \n"))
b=int(input("Enter the breadth : \n"))
print("Area of a rectangle is ",l*b)