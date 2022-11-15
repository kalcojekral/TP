def emso_leta_preracun():
    emso = input("Vnesi EMŠO: ")
    leto = emso[4:7]
    letnica = int(leto)
    if emso[4] == "9": 
        letnica = letnica + 1000
    else:
        letnica = letnica + 2000
    starost = 2022 - letnica
    print(starost)






emso_leta_preracun()