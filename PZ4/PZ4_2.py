#Программа, определяющая после какого дня суммарный пробег превысит
#200 км и выводит кол-во дней и суммарный пробег

P = input('Введите процент от 0 до 50: ')
K = 1
S = 10

while type(P) != float:
    try:
        P = float(P)
    except ValueError:
        print('Неверно ввели!')
        P = input('Введите процент от 0 до 50: ')

while P <= 0 or P >= 50:
    print('Неправильно ввели!')
    P = input('Введите процент от 0 до 50: ')
    while type(P) != float:
        try:
            P = float(P)
        except ValueError:
            print('Неверно ввели!')
            P = input('Введите процент от 0 до 50: ')

while S <= 200:
    S += S * (P / 100)
    K += 1

print('Количество дней: ', K, 'Суммарный пробег: ', S)