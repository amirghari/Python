import random
def dice():
    return random.randint(1, 6)
result = dice()
while result != 6:
    print(result)
    dice()
    result = dice()
print(result)














