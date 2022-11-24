import math

n=[]

m=int(input("Število elementov: "))

for i in range(0,m):
    ele=(int(input("Število: ")))

    n.append(ele)


def vrni(list):

    avg = sum(list)/len(list)
    
    najblizja = 0
    for i in list:
        razlika = abs(avg-i)
        if razlika < abs(avg-najblizja):
            najblizja = i
        


    print(max(list), min(list), avg, najblizja)



vrni(n)