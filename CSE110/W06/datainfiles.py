#numbers = [42, 25, 18, 83, 23, 85, 38, 2]
#largest = numbers[0]
#for number in numbers:
    #if number > largest:
        #largest = number
#print(f"The largest number is: {largest}")

#shopping_cart = [
    #["Chips", 2.99],
    #["Bread", 2.50],
   # ["Milk", 3.19],
  #  ["Ice Cream", 6.99],
  #  ["Cheese", 5.99],
#    ["Candy bar", 0.99]
#]
#max_price = -1
#max_producct = ""
#for item in shopping_cart:
 #   product_name = item[0]
  #  price = item[1]
   # if price > max_price:
  #       max_product = product_name
#print(f"The maximum price is: {max_price}")
#print(f"The product with the maximum price is: {max_product}")

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
age = 9999
name = ""
for person in people:
    info = person.split(" ")
    person_name = info[0]
    person_age = int(info[1])
    if person_age < age:
        age = person_age
        name = person_name
print(f"The youngest person is: {name} with an age of: {age}")
