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