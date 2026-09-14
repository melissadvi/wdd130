def main ():
    start = float(input("Enter the first odometer reading (miles): "))
    end = float(input("Enter the second odometer reading (miles): "))
    amount = float(input("Enter the amount of fuel used (gallons): "))
    miles = mile_per_gallon(start, end, amount)
    liters = lp100k_from_mpg (miles)
    print(f"{miles:.2f} miles per gallon")
    print(f"{liters:.2f} liters per 100 kilometers")
    pass
def mile_per_gallon(start, end, amount):
    return (end - start) / amount
def lp100k_from_mpg(miles):
    return 235.215 / miles
main()