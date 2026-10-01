# Project Milestone | Author: Melissa A. Vieira
# Enhancement: after the date and time of the receipt, print a message that tells the customer when to return their items. The return date should be 30 days from the current date and time. 
# The return time should be 9:00 PM on that day.

from datetime import datetime, timedelta
import csv 
def main ():
    try:
        products = read_dictionary('products.csv',0)
        print("Inkom Emporium")
        with open('request.csv','rt') as request_file:
            reader_second = csv.reader(request_file,delimiter=",")
            next(reader_second)
            total_items = 0
            subtotal = 0
            for row_second in reader_second:
                key_second = row_second[0]
                quantity_second = row_second[1]
                products_name = products[key_second][1]
                price = products[key_second][2]
                print(f"{products_name}: {quantity_second} @ {price}")
                total_items += int(quantity_second)
                subtotal += int(quantity_second) * float(price)
            print(f"Number of Items: {total_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {subtotal * 0.06:.2f}")
            print(f"Total: {subtotal * 1.06:.2f}")
            print("Thank you for shopping at the Inkom Emporium.")
            now = datetime.now()
            in_30days = now + timedelta(days=30)
            day_time = now.replace(hour=21, minute=0, second=0, microsecond=0)
            print(f"{now:%a %b %e %I:%M:%S %Y}")
            return_date = in_30days.replace(hour=day_time.hour, minute=day_time.minute, second=day_time.second, microsecond=day_time.microsecond)
            print(f"Please come back by {return_date:%a %b %e %I:%M:%S %p %Y} to return your items.")
    except FileNotFoundError as not_found_err:
        print("Error: missing file")
        print(not_found_err)
    except PermissionError as permission_err:
        print("Error: permission denied")
        print(permission_err)
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(key_err)

def read_dictionary(filename,key_column_index):
    dictionary = {}
    with open(filename,'rt') as products_file:
        reader = csv.reader(products_file,delimiter=",")
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary [key] = row
    return dictionary

if __name__ == "__main__":
    main()