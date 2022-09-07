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