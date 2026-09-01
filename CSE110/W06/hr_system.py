way = "/home/melvieira/Downloads/hr_system.txt"
with open(way) as f:
    next(f)
    content = f.readlines()
for line in content:
        parts =line.split(" ")
        name = parts[0]
        id = int(parts[1])
        job_title = parts[2]
        salary = int(parts[3])
        paycheck = salary /24
        if job_title.lower() == "engineer":
            paycheck_amount = salary /24 + 1000
        else:
            paycheck_amount = paycheck
        print(f"{name} (ID: {id}), {job_title} - ${paycheck_amount:.2f}")

with open("life-expectancy.csv") as life:
    next(life)
    for line in life:
        print(line.strip().split(","))
    for line in life:
        year = input("Enter the year of interest: ")
        parts = line.strip().split(",")
        expectancy = parts[3]
        if expectancy == parts[0]:
            print(f"The overall max life expectancy is: {parts[1]} in {parts[0]}")