import math


#square
side = float(input("What is the length of a side of the square? "))
square_area = side ** 2 #calcute the area of the square
print(f"The area of the square is {square_area}")

#rectangle
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))

rectangle_area = length * width #calcute the area of the rectangle
print(f"The area of the rectangle is {rectangle_area}")
#print(f"The area of the rectangle is {length * width:.2f}")

#circle
radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * radius ** 2 
print(f"The area of the circle is {circle_area}")

#### The following work with square cms ####

#square
side = float(input("What is the length of a side of the square (in cm)? "))
square_area = side ** 2
print(f"The area of the square is {square_area} cm²")
area_in_meters = square_area / 10000
print(f"The area of the square is {area_in_meters} m²")

#rectangle
length = float(input("What is the length of the rectangle? (in cm) "))
width = float(input("What is the width of the rectangle? (in cm) "))

rectangle_area = length * width
rectangle_area_meters = rectangle_area / 10000 
print(f"The area of the rectangle is {rectangle_area}cm² or {rectangle_area_meters}m²")
#print(f"The area of the rectangle is {length * width:.2f}")

#circle
radius = float(input("What is the radius of the circle? (in cm) "))
circle_area = math.pi * radius ** 2 
circle_area_meters = circle_area / 10000
print(f"The area of the circle is {circle_area} cm² or {circle_area_meters} m²")