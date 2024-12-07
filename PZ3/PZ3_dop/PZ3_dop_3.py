num1 = int(input('Введите двузначное число: '))

while num1 <= 9 or num1 >= 100:
    print('Введите двузначное число!')
    num1 = int(input('Введите двузначное число: '))

num2, num3 = divmod(num1, 10)

print(num1 + 2 if (num2 + num3) % 2 == 0 else num1 - 2)