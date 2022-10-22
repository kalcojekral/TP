
prastevila = []

for i in range (1, 50) :
    if i == 0 or i == 1 :
        continue
    else :
        for j in range (2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prastevila.append(i)


print(prastevila)