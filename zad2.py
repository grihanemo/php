x1 = []
x2 = ''
file = open("numbers.csv")
mf = file.read()
file.close()

for i in range(0,len(mf)):
    if mf[i] == ',':
        x1.append(int(x2))
        x2=str()
    else:
        x2 = x2 + mf[i]
x1.append(int(x2))
y = sorted(x1)
print(y)
