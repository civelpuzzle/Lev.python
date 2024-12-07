#Проверка на истинность высказывания: "Число B находится между
#числами А и С".

a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')

while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неверно ввели!')
        a = input('Введите первое число: ')

while type(b) != int: #Обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Неверно ввели!')
        b = input('Введите второе число: ')

while type(c) != int: #Обработка исключений
    try:
        c = int(c)
    except ValueError:
        print('Неверно ввели!')
        c = input('Введите третье число: ')

print(a > b > c or c > b > a)

