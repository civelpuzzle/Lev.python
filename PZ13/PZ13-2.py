#В двумерном списке элементы последнего столбца заменить на -1.
import random

spis =[[random.randint(-5, 5) for i in range(3)] for i in range(3)]

print("Исходная матрица")
for i in spis:
    print(i)

spis = list(map(lambda x: x[:-1] + [-1], spis))

print("Конечная матрица")
for i in spis:
    print(i)