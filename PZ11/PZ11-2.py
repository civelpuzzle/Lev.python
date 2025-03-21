#Из предложенного текстового файла (text18-7.txt) вывести на экран его
#содержимое, количество букв в нижнем регистре. Сформировать новый файл,
#в который поместить текст в стихотворной форме предварительно поставив
#последнюю строку между второй и третьей.

kolvo_low = 0

for i in open('text18-7 (3).txt', encoding='utf-16'):
    for j in i:
        if j.islower():
            kolvo_low += 1


f1 = open('text18-7 (3).txt', encoding='utf-16')
print(f1.read())
print('Количество букв в нижнем регистре: ', kolvo_low)
f1.close()

f1 = open('text18-7 (3).txt', encoding='utf-16')
nt = f1.readlines()
nt[2], nt[3], nt[4], nt[5], nt[6] = nt[6] + '\n', nt[2], nt[3], nt[4], nt[5]
#print(nt)
f1.close()

f1 = open('newtext.txt', 'w', encoding='utf-16')
f1.writelines(nt)
f1.close()