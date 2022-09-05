talents = input("Enter talents.")
pounds = input("Enter pounds.")
lots = input("Enter lots")

firstGrams = int(talents) * 20 * 32 * 13.3
secondGrams = int(pounds) * 32 * 13.3
thirdGrams = int(lots) * 13.3

overallGrams = firstGrams + secondGrams + thirdGrams
kiloGrams = overallGrams/1000
grams = overallGrams % 1000


print(f"The Weight in modern units is : {kiloGrams:3.0f} kilograms and {grams:.2f} grams")
