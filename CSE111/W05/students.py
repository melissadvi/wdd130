import csv 
            
def main ():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary('students.csv',KEY_INDEX)
    inumber = input("Please Enter an I Number: ")
    inumber = inumber.replace("-","")
    if not inumber.isdigit():
       print("Invalid I-Number")
    elif len(inumber) !=9:
        print("An I-number must be 9 digits long")
    else:
       if inumber in students:
            student = students[inumber]
            name = student[NAME_INDEX]
            print(f"The student's name is {name}.")
       else:
            print("No such student")

def read_dictionary(filename,key_column_index):
    dictionary = {}
    with open(filename,'rt') as students_file:
        reader = csv.reader(students_file,delimiter=",")
        next(reader)
        for row in reader:
            key_value = row[key_column_index]
            dictionary [key_value]=row
    return dictionary

if __name__ == "__main__":
    main()
