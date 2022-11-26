"""
program to calculate radius of the circle
step 1 : Take the input from user (radius)
step 2 : calculate the area = pi*r2
step 3 : print result to console
"""
from math import pi
radius = float(input("Enter the radius of the circle : "))
area = round(pi * (radius ** 2),3)

print(f"The area of the circle is = {area}")