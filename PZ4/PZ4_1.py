#Программа, находящая произведение всех целых чисел от A до B
#включительно

a = input('Введите первое число: ')
b = input('Введите второе число: ')
sub = 0

while type(a) != int: #обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели')
        a = input('Введите первое число: ')

while type(b) != int: #обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели')
        b = input('Введите второе число: ')

while a <= b:
    sub = sub + a * b
    a += 1

print('Произведение целых чисел: ', sub)