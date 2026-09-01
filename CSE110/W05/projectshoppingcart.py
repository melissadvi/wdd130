# Project: Shopping Cart
# Creative part: "apply discount code"
print("Welcome to the Shopping Cart Program!")

selects = ["Add item", "View cart", "Remove item", "Compute total", "Apply Discount Code", "Quit"]
items = []
prices = []
discount_percent = 0.0

action = 0

while action != 6:
    print("Please select one of the following: ")
    for i in range(len(selects)):
        select = selects[i]
        count = i + 1
        print(f"{count} - {select}")
    action = int(input("Please enter an action: "))
    if action == 1:
        new_item = input("What item would you like to add? ")
        price = float(input(f"What is the price of {new_item}? "))
        items.append(new_item)
        prices.append(price)
        print(f"{new_item} has been added to the cart.")
    elif action == 2:
        print("The contents of the shopping cart are: ")
        for i in range(len(items)):
            print(f"{i + 1} {items[i]} - ${prices[i]:.2f}")
    elif action == 3:
            item_number = int(input("Which item would you like to remove? "))
            index = item_number - 1
            items.pop(index)
            prices.pop(index)
            print("Item removed.")
    elif action == 4:
        subtotal = sum(prices)
        discount_amount = subtotal * discount_percent
        final_total = subtotal - discount_amount
        print(f"Subtotal: ${subtotal:.2f}")
        if discount_percent > 0:
            print(f"Discount ({int(discount_percent * 100)}%): -${discount_amount:.2f}")
        print(f"Total: ${final_total:.2f}")
    elif action == 5:
        coupon = input("Do you have a discount cooupon? (yes/no): ").lower()
        if coupon == "yes" or coupon == "y":
            code = input("Please enter the coupon code: ").upper()
            if code == "SHOPPING10" or code == "CART10":
                discount_percent = 0.10
                print("Coupon applied! You got 10% off.")
            elif code == "SHOPPINGCART20": 
                discount_percent= 0.20
                print("Coupon applied! You got 20% off.")
            else:
                print("Invalid coupon code.")
    elif action == 6:
        print("Thank you. Goodbye!")
    else:
        print("Invalid entry. Pleqase choose a option from 1 to 5.")