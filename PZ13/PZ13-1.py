#В двумерном списке элементы строки N (N задать с клавиатуры)
#увеличить на 3.
import random

spis = [[random.randint(-5, 5) for i in range(3)] for i in range(3)]

print("Исходная матрица")
for i in spis:
    print(i)

N = input("Введите номер строки: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите номер строки: ")

print(list(map(lambda x: x + 3, spis[N - 1])))