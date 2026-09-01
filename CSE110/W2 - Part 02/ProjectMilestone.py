#Project Milestone: Meal Price Calculator
#Ceative Part: Added an option for users the price and quantity of drinks consumed with the meal in the subtotal.

#1 - Ask the user for the price of a child and an adult meal
price_child = float(input("What is the price of a child's meal? "))
price_adult = float(input("What is the price of an adult's meal? "))

#2 - Creativity Part: drink price
price_drink = float(input("What is the price of a drink? "))

#3 - Ask the user for the number of adults and children 
many_child = int(input("How many children are there? "))
many_adult = int(input("How many adults are there? "))

#4 - Creativity Part: drink quantity
many_drink = int(input("How many drinks are there? "))

#5 - Compute and display subtotal 
subtotal = (price_child * many_child) + (price_adult * many_adult) + (price_drink * many_drink)
print (f"Subtotal: ${subtotal:.2f}")

#6 - Sales tax rate 
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * (tax_rate/100)
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

#7 - Payment Amount
payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}") 