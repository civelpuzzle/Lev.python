#Описать функцию AddRightDigit(D, K), добавляющую к целому
#положительному числу K справа цифру D (D - входной параметр целого
#типа, лежащий в диапазоне 0-9, K - параметр целого типа, являющийся
#одновременно входным и выходным). С помощью этой функции
#последовательно добавить к данному числу K справа данные цифры D1
#D2, выводя результат каждого добавления.

import random

K = input("Введите целое число: ")
D = 0

def proof(a):
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print("Неправильно ввели")
            a = input("Введите число: ")
    return a

def AddRightDigit(a, b):
    a = random.randint(0, 9)
    b = b * 10 + a
    return b

K = proof(K)
K = AddRightDigit(D, K)
print(K)
K = AddRightDigit(D, K)
print(K)