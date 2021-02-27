print("Ввести число от 1-10")
x = int(input())
print("Задайте степень от 0-9")
y = int(input())
x1 = int(x)
if y == 1:
    print(x)
if y == 0:
    print(1)
if x < 1 or x > 11:
    print("ошибка ввода")
if y < 0 or y > 10:
    print("ошибка ввода2")
else:
    for i in range(0,y-1):
        x1 = x1 * x
print("Ответ =",x1)
