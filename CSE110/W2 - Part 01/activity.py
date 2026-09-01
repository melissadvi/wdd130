age = input("How old are you? ")
age_number = int(age) + 1
print(f"On your next birthday, you will be {age_number}")

eggs_cartons = input("How many cartons of eggs do you have? ")
total_eggs = int(eggs_cartons) * 12
print(f"You have {total_eggs} eggs")

cookies = input("How many cookies do you have? ")
cookies_person = input("How many people are there? ")
cookies_per_person = int(cookies) / int(cookies_person)
print(f"Each person may have {cookies_per_person} cookies")