#Дан список размера N. Возвести в квадрат все его локальные
#минимумы (то есть числа, меньше своих соседей

import random

N = input("Введите размер списка: ")
user_list = []
loc_min = []

while type(N) != int: #обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели!')
        N = input("Введите размер списка: ")

for i in range(N):
    user_list.append(random.randint(-100, 100))

for i in range(1, len(user_list) - 1):
    if user_list[i] < user_list[i - 1] and user_list[i] < user_list[i + 1]:
        loc_min.append(user_list[i])

#print(user_list)
#print(loc_min)

for i in range(len(loc_min)):
    loc_min[i] = loc_min[i] ** 2

print('Локальные минимумы в квадрате: ', loc_min)