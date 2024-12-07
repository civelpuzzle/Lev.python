num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
mult = num1 * num2

if mult < 0:
    mult = mult * 8
    print('Результат умножения на 8: ', mult)
else:
    mult = mult * 1.5
    print('Результат умножения на 1.5: ', mult)