# Problem 1
names = []

while True:
    name = input("Enter a name: ")
    if name == "END":
        break
    names.append(name)

name_string = ""
for i in names[:-1]:
    name_string += i+", "
name_string += names[-1]

print("The names are: "+name_string)
