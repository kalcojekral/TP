import random

x = random.randrange(0,30)
s_poskusov = 5

while s_poskusov > 0:
    poskus = input("Vnesi število: ")
    poskus = int(poskus)
    if x == poskus:
        print("Zmaga")
        break
    elif poskus < x:
        print("Premalo")
    else:
        print("Preveč")
    s_poskusov = s_poskusov-1



'''c = 0
x = 15

while c<5: 
    c = c+1
    y=int(input("Vnesi število od 0 do 30: "))

    if y<x:
        print("Premalo")

    elif y>x:
        print("Prevec")

    else:
        print("Bravo")'''
