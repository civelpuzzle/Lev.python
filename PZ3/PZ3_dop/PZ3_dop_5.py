num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = num1 + num2

print(num3 + 1 if num3 % 5 == 0 else num3 - 2)