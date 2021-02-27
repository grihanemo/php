import random
x = 100
file = open("numbers.csv", "w+")
for i in range(0,x):
    file.write(str(random.randint(1,100)))
    if i != x-1: 
        file.write(",")
file.close()
