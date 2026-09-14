#Project: Tire Volume | Author: Melissa A. Vieira
#Creative Part: When the user answer yes to buy the tires, the program will ask for their phone number and save it to the file along with the tire information. If they answer no, only the tire information will be saved.
import math
from datetime import datetime

width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the wheel in inches (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = (math.pi * width ** 2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000
print(f"The approximate volume is {volume:.2f} liters")

phone_number = " "
choice = input("Do you want to buy these tires? (yes/no): ").strip().lower()
if choice == "yes":
    phone_number = input("Enter your phone number: ").strip()

current_date = datetime.now()

with open("volumes.txt", mode="at") as volume_file:
    if choice == "yes":
        print(f"{current_date:%Y-%m-%d}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}, Phone: {phone_number}", file=volume_file)
    else:
        print(f"{current_date:%Y-%m-%d}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}", file=volume_file)

print("Thank you for using our tire service! Your information has been saved.")