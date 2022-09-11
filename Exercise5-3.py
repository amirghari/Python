number = int(input("Enter a Number"))
if number == 2 or number == 3 or number == 5 or number == 7 or number == 11:
    print("This number is a prime number")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
    print("This number is not a prime number")
else:
    print("This number is a prime number")