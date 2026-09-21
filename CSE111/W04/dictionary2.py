# example 02: compound value
def main():
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3
    total = 0
    for value in students_dict.values():
        credits = value[CREDITS_INDEX]
        total += credits
    print("-" * 50)
    print(f"Total credits earned by all students: {total}")
if __name__ == "__main__":
    main()
