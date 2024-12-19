#Дан список размера N. Найти минимальный из его локальных максимумов
#(локальный минимум - это элемент, который меньше любого из своих
#соседей).

import random

N = input("Введите размер списка: ")
user_list = []
loc_max = []

while type(N) != int: #обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели!')
        N = input("Введите размер списка: ")

for i in range(N):
    user_list.append(random.randint(-100, 100))

for i in range(1, len(user_list) - 1):
    if user_list[i] > user_list[i - 1] and user_list[i] > user_list[i + 1]:
        loc_max.append(user_list[i])

#print(user_list)
#print(loc_max)
print('Минимальный локальный максимум: ', min(loc_max))