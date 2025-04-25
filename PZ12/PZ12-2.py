#Составить генератор (yield), который преобразует все буквенные
#символы в строчные.

stroka = input("Введите строку: ")
def zad(a):
    b = a.split()
    yield from [i.lower() for i in b]

hran = zad(stroka)

for i in hran:
    print(i)