import random

total = 0
numruns = 1000000
for i in range(numruns):
    x= random.randint(1,7)
    y= random.randint(1,7)

    maxVal = max(x,y)
    if (maxVal <= 4):
        total += 1

print(total/numruns)