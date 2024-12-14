#Программа, находящая произведение всех целых чисел от A до B
#включительно

sub = 0
a = input('Введите первое число: ')
b = input('Введите второе число: ')

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
    sub += a * b
    a += 1

print('Произведение целых чисел: ', sub)