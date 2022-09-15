names = set()
names = {"Amir", "Mammad", "Abdol", "Hasan", "Helia"}
inputName = input("Enter a name.")
while inputName != "":
    for name in names:
        if inputName == name:
            print("Existing Name")
    names.add(inputName)
    inputName = input("Enter a name.")
print("The program is stopped!")