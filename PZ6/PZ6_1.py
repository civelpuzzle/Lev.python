#Дан целочисленный список размера 10. Вывести все содержащиеся в
#данном списке нечётные числа в порядке возрастания их индексов, а
#также их количество К.

import random

user_list = []
nech_list = []
K = 0

for i in range(10):
    user_list.append(random.randint(-100, 100))

for i in user_list:
    if i % 2 != 0:
        nech_list.append(i)
        K += 1

print('Нечётные числа: ', nech_list)
print('Количество: ', K)