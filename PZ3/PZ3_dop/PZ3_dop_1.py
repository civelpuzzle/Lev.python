#Ввести 2 числа. Если их произведение отрицательно, умножить его на 8,
#в противном случае увеличить его в 1.5 раза

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
mult = num1 * num2

if mult < 0:
    mult = mult * 8
    print('Результат умножения на 8: ', mult)
else:
    mult = mult * 1.5
    print('Результат умножения на 1.5: ', mult)