#Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти минимальные продажи по
#каждому виду продукции, результаты вывести на экран.

str_prod = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
str_prod = str_prod.split()

slov1 = dict.fromkeys([str_prod[0]], str_prod[1:6])
znach1 = str_prod[0]
slov2 = dict.fromkeys([str_prod[6]], str_prod[7:])
znach2 = str_prod[6]
def funcc(a, b):
    nums = a.get(b)
    spis = []
    for i in range(len(nums)):
        spis.append(int(nums[i]))
    print('Минимальное кол-во продукции: ', min(spis))

funcc(slov1, znach1)
funcc(slov2, znach2)