# 1. Suvedam sveiką teigiamą skaičių n (tarkim 100). Programa sugeneruoja atsitiktinį skaičių nuo 1 iki n Sugeneravus atsitiktinį skaičių vartotojui siūloma atspėti kokį skaičių sugeneravo programa. Įvedus spėjamą skaičių (tarkim 75) programa praneša ar sugeneruotas skaičius didesnis ar mažesnis už įvestą skaičių ir siūlo spėti dar kartą (tarkim „Sugeneruotas skaičius didesnis už 75. Atliksite 3 spėjimą...“). Įvedus bet kokius simbolius ar neigiamus skaičius programa prašo kartoti įvedimą ir jo neprisumuoja prie spėjimų skaičiaus. Vartotojui atspėjus skaičių rodomas pranešimas, koks buvo sugeneruotas skaičius ir kiek spėjimų buvo atlikta. Pabaigus žaidimą –siūloma sužaisti dar kartą. Žaidimo programavime panaudoti funkcijas
# Be žaidimo paslaugos programa sukuria žaidimo „registravimo“ failą reg.txt, kuriame yra pateikiama informacija apie žaidimo eigą. 
import random
zaidziam = True
kartai = 0
negalimi = 0
kiekZaide = 0
ataskaita = open('task01.txt', 'w', encoding='utf-8')

while zaidziam:
    zaidejoSkaicius = int(input("Iveskite sveika teigiama skaiciu: "))
    ataskaita.write(f'Zaidejas ivede skaiciu {zaidejoSkaicius}.\n')
    atsitiktinis = random.randint(1, zaidejoSkaicius)
    ataskaita.write(f'Kompiuteris sugeneravo skaiciu {atsitiktinis}.\n')
    kiekZaide +=1

    while zaidziam:
        spejimas = int(input("Spekite skaiciu: "))
        if 0 < spejimas < atsitiktinis:
            kartai += 1
            print(f'Sugeneruotas skaicius didesnis uz {spejimas}. Atliksite {kartai + 1}-a spejima.')
            ataskaita.write(f'{kartai}-uoju spejimu zaidejas ivede skaiciu {spejimas}. Kompiuterio sugeneruotas skaicius didesnis.\n')
        elif 0 < spejimas > atsitiktinis:
            kartai += 1
            print(f'Sugeneruotas skaicius mazesnis uz {spejimas}. Atliksite {kartai + 1}-a spejima.')
            ataskaita.write(f'{kartai}-uoju spejimu zaidejas ivede skaiciu {spejimas}. Kompiuterio sugeneruotas skaicius mazesnis.\n')
        elif spejimas == atsitiktinis:
            kartai += 1
            print(f'Teisingas spejimas;\nSpejimu skaicius: {kartai}.\nNegalimu spejimu skaicius: {negalimi}')
            ataskaita.write(f'{kartai}-uoju spejimu zaidejas ivede skaiciu {spejimas} ir atspejo teisingai.\nSpejimu skaicius: {kartai}.\nNegalimu spejimu skaicius: {negalimi}\n')
            zaidziam = False  
        else:
            print("Negalimas skaicius, bandykite dar karta.")
            negalimi += 1
            ataskaita.write(f'Zaidejas ivede negalima skaiciu - {spejimas}. Spejimas nesiskaito.\n')

    if atsitiktinis == spejimas:
        kartoti = input("Kartoti T/N? ")
        if kartoti == "T" or kartoti == "t":
            zaidziam = True
            kartai = 0
            negalimi = 0
            ataskaita.write(f'Zaidejas nusprende kartoti zaidima.\n')
        else:
            zaidziam = False
            ataskaita.write(f'Zaidejas nusprende zaidimo nekartoti.\nZaidejas zaide {kiekZaide} kartus/a.\n')

ataskaita.close()