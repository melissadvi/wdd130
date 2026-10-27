def main():
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis",
        "81-298-9238": "Sama Patel"
    }
    id = input("Enter a student ID: ")
    name = students.get(id)
    if name: 
        print(name)
        students.pop(id)
    else:
        print("No such student")
    print()
    for key, value in students.items():
        print(key, value)
if __name__ == "__main__":
    main()
    