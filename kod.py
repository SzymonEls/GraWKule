import random
#zmienne
licz = 0
pocz_kule = 10
kule = pocz_kule
g1 = 0
g2 = 0
g1_codal = []
g1_nau = []

#Przygotowywanie codal - g1
licznik5 = 0
while licznik5 != pocz_kule:
        g1_codal.append(0)
        licznik5 = licznik5 + 1

#Otwieranie doświadczenia - g1
plik = open('C:/Users/SzymonPC/Dysk Google/dokumenty/PYTHON - nauka/pliki programów/kule_gracz5.txt')
g1_nau_chwil = plik.readlines()
plik.close()

#Usuwanie znaków \n - g1
licznik4 = 0
while licznik4 != pocz_kule - 1:
        r = g1_nau_chwil[licznik4]
        r = r[:r.index("\n")]
        g1_nau_chwil[licznik4] = r
        print(licznik4)
        licznik4 = licznik4 + 1

#Zmiana doświadczenia na tablice int - g1
licznik6 = 0
while licznik6 != pocz_kule:
        akt = g1_nau_chwil[licznik6]
        akt = akt[:akt.index(' ')] + '*' + akt[akt.index(' ') + 1:]
        g1_nau.append([int(akt[akt.index('[') + 1:akt.index(',')]), int(akt[akt.index('*') + 1:akt.index(' ') - 1]), int(akt[akt.index(' ') + 1:akt.index(']')])])
        licznik6 = licznik6 + 1


#gra        
while licz != 100000:
    #print(g1_nau) - bez pisania
    while kule > 0:
        #Gracz1<<<<<<<<<<<<<<<<<<<<<<<<<

        #zmienne
        a = g1_nau[kule - 1][0]
        b = g1_nau[kule - 1][1]
        c = g1_nau[kule - 1][2]

        #DECYZJA na podstawie doświadczenia - g1
        wylosowana = random.randint(1, a + b + c)
        if wylosowana > 0 and wylosowana <= a:
            inp = 1
        if wylosowana > a and wylosowana <= b + a:
            inp = 2
        if wylosowana > b + a:
            inp = 3

        #Zapis decyzji - g1
        g1_codal[kule - 1] = inp
        
        
        kule = kule - int(inp)
        #print("kul po g1 {a}".format(a=kule)) - bez pisania
        
        
        #Jeśli koniec kul
        if kule <= 0:
            #print("Wygrywa gracz 1!!!") - bez pisania
            g1 += 1
            wygrana = "g1"
            break

        #Gracz2<<<<<<<<<<<<<<<<<<<<<<<<<<

        #Losowanie
        inp2 = random.randint(1, 3)

        kule = kule - int(inp2)
        #print("kul po g2 {b}".format(b=kule)) - bez pisania

        #Jeśli koniec kul
        if kule <= 0:
            #print("Wygrywa gracz 2!!!") - bez pisania
            g2 += 1
            wygrana = "g2"
            break

    #podsumowanie rundy - g1

    licznik2 = 0

    #info
    #print(g1_codal) - bez pisania

    #Analiza ruchów    
    if wygrana == "g1":
        while licznik2 != len(g1_codal):
            if g1_codal[licznik2] == 1:
                a = g1_nau[kule - 1][0]
                b = g1_nau[kule - 1][1]
                c = g1_nau[kule - 1][2]
                g1_nau[licznik2][0] += 1
        
            if g1_codal[licznik2] == 2:
                a = g1_nau[kule - 1][0]
                b = g1_nau[kule - 1][1]
                c = g1_nau[kule - 1][2]
                g1_nau[licznik2][1] += 1
            
            if g1_codal[licznik2] == 3:
                a = g1_nau[kule - 1][0]
                b = g1_nau[kule - 1][1]
                c = g1_nau[kule - 1][2]
                g1_nau[licznik2][2] += 1
    
            licznik2 += 1

    #info po rundzie
    #print("Runda: <<<<<<<<<<<<<<<<<<<<{c}".format(c=licz + 1)) - bez pisania

    #Zerowanie
    kule = pocz_kule
    
    licznik5 = 0
    while licznik5 != pocz_kule:
        g1_codal[licznik5] = 0
        licznik5 = licznik5 + 1

    licz += 1

#info po wszystkich rundach
print("Wygranych gracza1: {d}".format(d=g1))
print("Wygranych gracza2: {e}".format(e=g2))

#Zapis doświadczeń
plik2 = open('C:/Users/SzymonPC/Dysk Google/dokumenty/PYTHON - nauka/pliki programów/kule_gracz5.txt', 'w+')
licznik3 = 0
while licznik3 != pocz_kule:
       if licznik3 == pocz_kule - 1:
              plik2.write(str(g1_nau[licznik3]))
       else:
              plik2.write(str(g1_nau[licznik3]) + "\n")
       
       licznik3 = licznik3 + 1
plik2.close()
