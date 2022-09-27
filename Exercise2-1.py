user = input("Enter your Name")
print("Hello, " + user + "!")

# PART 2

radius = input("Enter the radius of the circle.")
numberRadius = int(radius)
multiRadius = numberRadius * numberRadius
area = 3.14 * multiRadius
print("The area of the circle is " + str(area) + " .")


# PART 3
length = input("Enter the Length of the rectangle.")
width = input("Enter the width of the rectangle.")

lengthInt = int(length)
widthInt = int(width)

area = lengthInt * widthInt
perimeter = 2 * (lengthInt + widthInt)

print("The area of the rectangle is " + str(area) + " and the perimeter of it is " + str(perimeter) + " .")

# PART 4

number1 = input("Enter the first number")
number2 = input("Enter the second number")
number3 = input("Enter the third number")

sums = int(number1) + int(number2) + int(number3)
product = int(number1) * int(number2) * int(number3)
average = sums/3

print("Sum of the numbers is " + str(sums) + ", product is " + str(product) + " and the average is " + str(average) + ".")


# PART 5

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

# PART 6

import random
print(f"{random.randrange(1, 6) :03d}")
print(f"{random.randrange(1, 6) :03d}")