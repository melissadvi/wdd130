# example 01: simple value
def main():
    students_dicts = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }
    
    students_dicts["81-298-9238"] = "Sama Patel" #dictionary_name[key] = value
    students_dicts.pop("61-315-0160")
    length = len(students_dicts)
    print(f"length: {length}")
    print(students_dicts)
    print()
    print("-" * 50)
    id = input("Enter a student ID: ")
    if id in students_dicts: #if key in dictionary_name:
        name = students_dicts[id] #value = dictionary_name[key]
        print(name)
    else:
        print("No such student")
    print("-" * 50)
if __name__ == "__main__":
    main()