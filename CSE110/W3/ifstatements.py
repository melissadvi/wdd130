temperature = float(input("What is your temperature in degress Celsius? "))
if temperature > 40.5:
   print("Go to the hospital!")
elif temperature > 39.4:
   print("Call your doctor.")
else:
   print("Consider rest or medicine.")
print("Have a good day.")