points_scored = [24, 18, 31, 42, 28]

running_total = 0
for amount in points_scored:
    #running_total = running_total + amount
    running_total += amount

print(f"The player has scored {running_total} points")

receipts = [12.24, 18.50, 4.99, 21.75]

total = 0
for receipt in receipts:
    total += receipt

print(f"The total is: {total:.2f}")