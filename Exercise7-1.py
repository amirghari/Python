seasons = ("winter", "spring", "summer", "autumn")
month = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
number = int(input("Please enter the number of your month"))
for i in range(4):
    if number in month[i]:
        print(seasons[i])