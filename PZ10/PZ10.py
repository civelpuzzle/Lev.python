#Туристические агентства предлагают следующие туры. Вояж – Мексика,
#Канада,Израиль,Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР.
#Радуга – США,Испания,Швеция, Австралия.
#Определить в каких турагенствах можно приобрести туры в Канаду,
#а в каких в США

voiazh = {'Мексика', "Канада", "Израиль", "Италия", "США"}
v1 = "Вояж"
reinatur = {"Англия", "Япония", "Канада", "ЮАР"}
re1 = "РейнаТур"
rainbow = {"США", "Испания", "Швеция", "Австралия"}
ra1 ="Радуга"

otvet1 = []
otvet2 = []
Kanada = {"Канада"}
USA = {"США"}

def otv(a, b):
    if a & Kanada != set():
        otvet1.append(b)
    if a & USA != set():
        otvet2.append(b)
    return otvet1, otvet2;

otv(voiazh, v1)
otv(reinatur, re1)
otv(rainbow, ra1)

print(f"Можно приобрести туры в Канаду: {otvet1}. В США: {otvet2}")