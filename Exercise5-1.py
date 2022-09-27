import random
numbers = []
sum = 0
times = int(input("How many dice to roll?"))
for x in range(times):
    dice = random.randint(1, 6)
    numbers.append(dice)
    sum += dice
print(numbers)
print("The sum of the dices is " + str(sum) + ".")

# PART2

number = input("please enter a number.")
list_number = []
while number != "":
    list_number.append(int(number))
    number = input("please enter a number.")
list_number.sort(reverse=True)
print(list_number)


# PART3

number = int(input("Enter a Number"))
if number == 2 or number == 3 or number == 5 or number == 7 or number == 11:
    print("This number is a prime number")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
    print("This number is not a prime number")
else:
    print("This number is a prime number")


# PART4


city_list = []
x = 5
for i in range(5):
    city = input("Enter the city name")
    city_list.append(city)
for i in range(5):
    print(city_list[5-x])
    x -= 1

