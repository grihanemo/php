print("Введите слово или фразу")
x = str(input())
y1 = len(x) - 1
y2 = 0
for i in range (0,len(x)-1):
    if x[y1] == x[y2]:
        y1 = y1 - 1
        y2 = y2 + 1
    else:
        print("не является палиндромом")
        quit()
print("это палиндром")
