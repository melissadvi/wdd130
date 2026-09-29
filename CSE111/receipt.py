# Project Milestone | Author: Melissa A. Vieira

import csv 
def main ():
    products = read_dictionary('products.csv',0)
    print("All Products")
    print(products)
    print("Requested Items")
    with open('request.csv','rt') as request_file:
        reader_second = csv.reader(request_file,delimiter=",")
        next(reader_second)
        for row_second in reader_second:
            key_second = row_second[0]
            quantity_second = row_second[1]
            products_name = products[key_second][1]
            price = products[key_second][2]
            print(f"{products_name}: {quantity_second} @ {price}")

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