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
