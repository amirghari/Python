seasons = ("winter", "spring", "summer", "autumn")
month = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
number = int(input("Please enter the number of your month"))
for i in range(4):
    if number in month[i]:
        print(seasons[i])

# Part2

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
print(names)

# PART 3


dashboard = {}
def askingInfo():
    print("Choose what you want to do:")
    print("n: add new airport")
    print("f: fetch airport name")
    print("Press ENTER to quit program")
    return input()

query = askingInfo()
while query == "n" or query == "f":
    if query == "n":
        newIcao = input("Enter ICAO code: ")
        newName = input("Enter name of airport: ")
        dashboard.update({newIcao: newName})
    else:
        icao = input("Enter ICAO code: ")
        if icao in dashboard:
            print("Airport name:", dashboard[icao])
        else:
            print("Airport did not found")
    query = askingInfo()
print("Bye!")