#Project Milestone: Data Analysis
#Creative Part: Menu Intercative
#This program contains an interactive menu that allows the user to search for life expectancy statistics either by year or by a specific country.

print("=" * 60)
print("Global Life Expectancy Data Analysis")
print("=" * 60)

keep_running = True

while keep_running:
    print("\n" + "-" * 60)
    print("Main Menu")
    print("-" * 60)
    print("1. Analyze Life Expectancy Data of Interest")
    print("2. Search Statistics of Life Expectancy Data")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        print("\n" + "-" * 60)

        max_expectancy = 0
        min_expectancy = 9999
        max_country = ""
        min_country = ""
        max_year = ""
        min_year = ""
        max_year_expectancy = 0
        max_year_country = ""
        min_year_expectancy = 9999
        min_year_country = ""
        total_expectancy = 0
        count_year = 0

        year = input("Enter the year of interest: ")

        with open("life-expectancy.csv") as life:
             next(life)
             for line in life:
                 parts = line.strip().split(",")
                 country = parts[0]
                 year_file = parts[2]
                 expectancy = float(parts[3])
                 if expectancy > max_expectancy:
                     max_expectancy = expectancy
                     max_country = country
                     max_year = year_file
                 if expectancy < min_expectancy:
                     min_expectancy = expectancy
                     min_country = country
                     min_year = year_file
                 if year_file == year:
                     total_expectancy += expectancy
                     count_year += 1
                 if expectancy > max_year_expectancy:
                     max_year_expectancy = expectancy
                     max_year_country = country
                 if expectancy < min_year_expectancy:
                     min_year_expectancy = expectancy
                     min_year_country = country
        print()
        print(f"The overall max life expectancy is: {max_expectancy} from {max_country} in {max_year}")
        print(f"The overall min life expectancy is: {min_expectancy} from {min_country} in {min_year}")
        print()
        if count_year > 0:
            average_expectancy = total_expectancy / count_year
            print(f"For the year {year}:")
            print(f'The average life expectancy across all countries was {average_expectancy:.2f}')
            print(f"The max life expectancy was in {max_year_country} with {max_year_expectancy}")
            print(f"The min life expectancy was in {min_year_country} with {min_year_expectancy}")
        else:
            print(f"No data found for the year {year}.")   
    elif choice == "2":
        print("\n" + "-" * 60)
        target_country = input("Enter a country name to search: ").strip()

        country_max = 0
        max_c_year = ""
        country_min = 9999
        min_c_year = ""
        country_total = 0
        country_count = 0

        with open("life-expectancy.csv") as life:
            next(life)
            for line in life:
                parts = line.strip().split(",")
                country = parts[0]
                year_file = parts[2]
                expectancy = float(parts[3])
                if country.lower() == target_country.lower():
                    country_total += expectancy
                    country_count += 1
                    if expectancy > country_max:
                        country_max = expectancy
                        max_c_year = year_file
                    if expectancy < country_min:
                        country_min = expectancy
                        min_c_year = year_file
        print()
        if country_count > 0:
            print(f"Historical stats for {target_country.title()}:")
            print(f"The average life expectancy was {country_total / country_count:.2f}")
            print(f"The max life expectancy was {country_max} in {max_c_year}")
            print(f"The min life expectancy was {country_min} in {min_c_year}")
        else:
            print(f"No data found for {target_country.title()}.")
    elif choice == "3":
        print("Exiting the program and Thank you for using it. Goodbye!")
        keep_running = False
    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")


