import random
def dice():
    return random.randint(1, 6)
result = dice()
while result != 6:
    print(result)
    dice()
    result = dice()
print(result)

#PART 2
import random
side = int(input("Enter the sides"))
def dice(times):
    return random.randint(1, times)
result = dice(side)
while result != side:
    print( "dice " + str(result))
    result = dice(side)
print("dice " + str(result))

#PART 3

times = int(input("Enter Gallons"))
def conversion(gallons):
    return gallons * 3.78
if times > 0:
    litter = conversion(times)
    print(f"conversion to Litter is {litter}")
else:
    print("Enter a positive number.")

#PART 4

times = int(input("Enter Gallons"))
def conversion(gallons):
    return gallons * 3.78
if times > 0:
    litter = conversion(times)
    print(f"conversion to Litter is {litter}")
else:
    print("Enter a positive number.")

#PART 5
def evenMaker(lists):
    for list in lists:
        result = list % 2
        if (float(result) != 0):
            lists.remove(list)
    return lists




numberList = []
number = int(input("Enter a number to add it to the list. In case you want to stop enter 0. "))
while number != 0:
    numberList.append(number)
    number = int(input("Enter a number to add it to the list. In case you want to stop enter 0. "))
print(numberList)
print(evenMaker(numberList))

#PART 6

def pricePerUnit(diameter,price):
    area = float((3.14 * (diameter/2) * (diameter/2)) / 100)
    preicePerSqueredmeter = price/area
    return preicePerSqueredmeter
firstInputPrice = int(input("Enter the price of the first pizza in euro"))
firstInputDiameter = int(input("Please enter the diameter of the first pizza in cm."))

secondInputPrice = int(input("Enter the price of the second pizza in euro"))
secondInputDiameter = int(input("Please enter the diameter of the second pizza in cm."))

priceEfficiency1 = pricePerUnit(firstInputDiameter, firstInputPrice)
priceEfficiency2 = pricePerUnit(secondInputDiameter, secondInputPrice)

if (priceEfficiency1 < priceEfficiency2):
    print("First Pizza is more economical")
else:
    print("Second Pizza is more economical")



























