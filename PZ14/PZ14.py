#В исходном файле (Dostoevsky.txt) найти все годы деятельности писателя
#(например, 1821 года, 1837 год, 1843 году и так далее по всему тексту).
#Посчитать количество полученных элементов.

import re

f1 = open('Dostoevsky.txt')
ff = f1.read()
f1.close()

years = re.findall(r"\b(18[0-9]{2}\sг\w+)\b", ff)
print(years)

kolvo = len(years)
print("Количество полученных элементов: ", kolvo)