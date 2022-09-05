length = input("Enter the Length of the rectangle.")
width = input("Enter the width of the rectangle.")

lengthInt = int(length)
widthInt = int(width)

area = lengthInt * widthInt
perimeter = 2 * (lengthInt + widthInt)

print("The area of the rectangle is " + str(area) + " and the perimeter of it is " + str(perimeter) + " .")
