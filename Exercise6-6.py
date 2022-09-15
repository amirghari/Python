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