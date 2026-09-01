names = []
new_name = ""
while new_name != "end":
    new_name = input("Type the name of a friend: ")
    if new_name != "end":
        names.append(new_name)

print("Your friends are: ")
for name in names:
    print(f" {name}")





