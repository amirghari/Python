number = input("Enter a number")
if number != "":
    smallest = int(number)
    largest = int(number)
    while number != "":
        if int(number) < smallest:
            smallest = int(number)
        elif int(number) > largest:
            largest = int(number)
        number = input("Enter a number")
    print("Largest number is ",largest)
    print("Smallest number is",smallest)
else:
    print("Input a number.")

