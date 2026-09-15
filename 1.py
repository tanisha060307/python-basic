import math
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("rect area=", length*width)
print("rect perimeter=", 2*(length+width))

radi = float(input("Enter the radius of the circle: "))
print("circle area = ",math.pi*radi*radi)
print("circle perimeter = ", 2*math.pi*radi) 

side = float(input("Enter the side of the square: "))
print("square perimeter = ", 4*side)
print("square area = ", side*side)