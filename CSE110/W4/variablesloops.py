#payment = -1
#while payment < 0:
   #payment = float(input("What is the payment amount? "))

#print(f"The amount is ${payment:.2}.")

# The important thing to remember here is that when you first declare
# and intialize a variable, that determines the code block that it lives in.
# You can use it in blocks that are indented deeper than it, but shouldn't try
# to use it in any code blocks outside that indentation level. 

#number = 0
#while number <10:
    #number = int(input("What is the number? "))

#print("Finished with the loop.")

#number = 1
#while number <= 5: 
    #print(f"The number is: {number}")
    #number = number + 1

#print("Finished with the loop")

# Variable Scope
number = 0
name = ""

while number < 10:
    number = int(input("What is the number? "))
    name = input("What is your name? ")

print(f"Your name is: {name}")