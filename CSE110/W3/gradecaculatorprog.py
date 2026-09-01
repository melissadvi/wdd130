# ask the user for the grade
grade = float(input("What is the grade percent? "))

letter = ""

# figure out the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60 :
    letter = "F"

# get the last digit
last_digit = grade % 10

sign = ""
# determine the sign
if last_digit >= 7:
   sign = "+"
elif last_digit <3:
   sign = "-"
else:
   sign = "" 

# Handle exceptions (A+,F+,F-)
if letter == "A" and sign == "+":
    sign = ""  

if letter == "F":
    sign = ""
# display the letter grade
print(f"You have earned the grade {letter}{sign}")

if grade >= 70:
    print("Congratulations! You have passed the course!")
else:
    print("Sorry, please try the course again.")
