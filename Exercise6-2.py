import random
side = int(input("Enter the sides"))
def dice(times):
    return random.randint(1, times)
result = dice(side)
while result != side:
    print(result)
    result = dice(side)
print(result)














