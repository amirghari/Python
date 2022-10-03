number = 1
while number % 3 != 0:
    number += 1
    if number % 3 == 0 and 1000 > number > 1:
        print(str(f"The Number which is divisible by 3 is {number}"))
        number += 1
# PART2

inch = int(input("Please Enter your inch number to convert it to centimeters."))
while inch > 0:
    centi = inch * 2.54
    print(f"{inch} inches equal to {centi} centimeters")
    inch = int(input("Please Enter your inch number to convert it to centimeters."))
print('Execution stopped!')
# PART3

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
# PART4

import random
number = random.randint(1,10)
user_number = int(input("Enter your guess"))
while number != user_number:
    if number > user_number:
        print("Too low")
        user_number = int(input("Enter your guess"))
    elif number < user_number:
        print("Too high")
        user_number = int(input("Enter your guess"))
if number == user_number:
    print("correct")
# PART5

input_username = input("Enter your username")
input_password = input("Enter your password")
username = "python"
password = "rules"
attempts = 0
if username == input_username and password == input_password:
    print("welcome")
else:
    while (username != input_username or password != input_password) and attempts < 4:
        print("Please try again")
        input_username = input("Enter your username")
        input_password = input("Enter your password")
        attempts += 1
    if username == input_username and password == input_password:
        print("welcome")
    else:
        print("access denied")
# PART6
import random
times = 0
insidePoints = 0
totalPoints = int(input("How many points do we need for calculating pi?"))
while times < totalPoints:
    y = random.uniform(-1, 1)
    x = random.uniform(-1, 1)
    if x*x + y*y < 1:
        insidePoints += 1
    times += 1
print("pi is: ", 4*insidePoints/totalPoints)



