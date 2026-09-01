#format strings
number = 12.34567

print(f"The number is: ${number:.2f}")
print(number)

number = round(number, 3)
print(number)

number3 = 12.3011
number4 = round(number3, 2)
print(f"The number4 is ${number4:.2f}")

car_count = 5
print(f"There are {car_count} cars on the road.")
print("There are {} cars on the road.".format(car_count))

cars = 3
people = 8
people_per_car = people / cars
print(f"There are {people_per_car:.1f} people in each car.") #1 decimal
print(f"There are {people_per_car:.2f} people in each car.") #2 decimal
print(f"There are {people_per_car:.3f} people in each car.") #3 decimal

#scientific notation
distance = 9 * 1205 * 18
print(f"The distance is: {distance:.3e} meters") #scientific notation w 3digits
print(f"The distance is: {distance:.6e} meters") #scientific notation w 6digits

#thousands grouping
big_number = 123456789
print(f"The number is: {big_number}") #without formating
print(f"The number is: {big_number:,}") #with ","
print(f"The number is: {big_number:_}") #with "_"

length = 5
width = 10
area = length * width
print(f"The area of the rectangle is: {area} square units.")

import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area:.2f} square units.")

weight = 1.65
lower = math.floor(weight)
print(lower)
higher = math.ceil(weight)
print(higher)
