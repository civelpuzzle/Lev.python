#Вывод массы тела в килограммах

user_num = input('Введите номер единицы массы (1-5): ')
user_m = input('Введите массу тела: ')

while type(user_num) != int: #Обработка исключений
    try:
        user_num = int(user_num)
    except ValueError:
        print('Неправильно ввели!')
        user_num = input('Введите номер единицы массы (1-5): ')

while type(user_m) != float: #Обработка исключений
    try:
        user_m = float(user_m)
    except ValueError:
        print('Неправильно ввели!')
        user_m = input('Введите массу тела: ')

if user_num == 1:
    print(user_m, ' килограмм')
elif user_num == 2:
    user_m = user_m / 1000000
    print(user_m, ' килограмм')
elif user_num == 3:
    user_m = user_m / 1000
    print(user_m, ' килограмм')
elif user_num == 4:
    user_m = user_m * 1000
    print(user_m, ' килограмм')
elif user_num == 5:
    user_m = user_m * 100
    print(user_m, ' килограмм')
else:
    print('Неправильный номер единицы массы!')