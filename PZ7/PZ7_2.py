#Дана строка, содержащая полное имя файла, то есть имя диска, список
#каталогов (путь), собственно имя и расширение. Выделить из этой
#строки расширение файла (без предшествующей точки).

file_name = input('Введите имя файла: ')
dot = file_name.rfind('.')

file_name = file_name[dot + 1:]
print('Расширение файла: ', file_name)