#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""2014.oktober.17 Emelt szintu eretttsegi megoldasok Python programozasi nyelven. """
print("1. feladat")
"""Be kell olvasni az adatokat amit en szotarba gondoltam.Ami igy nezne ki.
szinhaz={
szamlalo{
"sor szama":
"szek szama":
"foglat":
"ar kategoria":
"ar":

 }
}
"""
szinhaz={}
n=0
szek = 0
sorok = 1
with open("foglaltsag.txt", "rt", encoding="utf-8")as f:
    for s in f:
        sor = s.replace("\n", "")
        for a in sor:
            n+=1
            szek+=1
            if szek == 21:
                sorok+=1
                szek=1
            szinhaz[n] = {}
            szinhaz[n]["sor szama"] = sorok
            szinhaz[n]["szek szama"] = szek
            if a == "x":
                szinhaz[n]["foglat"] = "foglalt"
            else:
                szinhaz[n]["foglat"] = "szabad"
        
n=0        
with open("kategoria.txt","rt",encoding="utf-8")as g:
    for er in g:
        sere =er.replace("\n","")
        for ser in sere:
            n+=1
            szinhaz[n]["ar kategoria"] = int(ser)
            if int(ser) == 1:
                szinhaz[n]["ar"] = 5000
            elif int(ser) == 2:
                szinhaz[n]["ar"] = 4000
            elif int(ser) == 3:
                szinhaz[n]["ar"] = 3000
            elif int(ser) == 4:
                szinhaz[n]["ar"] = 2000
            elif int(ser) == 5:
                szinhaz[n]["ar"] = 1500
        
        
with open("sem.txt","wt", encoding="utf-8") as h:
    for k, v in szinhaz.items():
        h.write("{0}:{1}\n".format(k,v))
#print(szinhaz)

print("2. feladat")
"""Be kell kerni egy szek es egy sor szamot es megmondani hogy foglat-e """
besor=int(input("Kerem irjon be egy sor szamot lehetoleg 1 es 15 kozott.: "))
beszek = int(input("Kerem irjon be egy szek szamot 1 es 20 kozott.: "))
for a in szinhaz.values():
    if a["szek szama"] == beszek and a["sor szama"] == besor:
        print("Ez a hely: {}".format(a["foglat"]))

print("3. feladat")
"""Hany szazalakat adtak el a jegyeknek ki kell iratni."""
eladot = 0
for a in szinhaz.values():
    if a["foglat"] == "foglalt":
        eladot+=1
print("Az eloadasra eddig {0} jegyet adtak el, ez a nezoter {1}%-a".format(eladot, round((eladot/len(szinhaz))*100)))

print("4. feladat")
"""Meg kell hatarozni hogy melyik arkategoriaban adtak el a legtobb jegyet."""
arkategoria = {
    "1.":0,
    "2.":0,
    "3.":0,
    "4.":0,
    "5.":0
}
for a in szinhaz.values():
    if a["foglat"] == "foglalt" and a["ar kategoria"] == 1:
        arkategoria["1."]+=1
    elif a["foglat"] == "foglalt" and a["ar kategoria"] == 2:
        arkategoria["2."]+=1
    elif a["foglat"] == "foglalt" and a["ar kategoria"] == 3:
        arkategoria["3."]+=1
    elif a["foglat"] == "foglalt" and a["ar kategoria"] == 4:
        arkategoria["4."]+=1
    elif a["foglat"] == "foglalt" and a["ar kategoria"] == 5:
        arkategoria["5."]+=1
#print(arkategoria)
n=0
for k,v in sorted(arkategoria.items(), key=lambda v:v):
    n+=1
    if n == len(arkategoria): 
        print("A legtobb jegyet a(z) {} arkategoriaban ertekesitettek.".format(k))

print("5. feladat")
"""Bevetelt ki kell szamolni. """
bevetel=0
for a in szinhaz.values():
    if a["foglat"] == "foglalt":
        bevetel+=a["ar"]
print("A szinhaznak eddig {} bevetele van.".format(bevetel))
print("6. feladat")
"""Egyedulallo jegyek keresese. """


for k,v in szinhaz.items():
    if v['foglat'] == "foglalt":
        szinhaz[k]['egyedulallo'] = False
        continue
    if v['szek szama'] == 1 and szinhaz[k+1]['foglat'] == "foglalt":
        szinhaz[k]['egyedulallo'] = True
        continue
    if v['szek szama'] == 20 and szinhaz[k-1]['foglat'] == "foglalt":
        szinhaz[k]['egyedulallo'] = True
        continue
    if v['szek szama'] != 1 and v['szek szama'] != 20 and szinhaz[k+1]['foglat'] == "foglalt" and szinhaz[k-1]['foglat'] == "foglalt":
        szinhaz[k]['egyedulallo'] = True
        continue
    szinhaz[k]['egyedulallo'] = False

egyedulalo = 0
for a in szinhaz.values():
    if a["egyedulallo"]:
        egyedulalo+=1
print("Oszesen {} szabad, egyedulallo hely van".format(egyedulalo))

print("7. feladat")
"""ki kell  irni a szabad helyek es a hozza tartozo arakat
"""
sor = 1
with open("szabad.txt","wt",encoding="utf-8") as d:
    for v in szinhaz.values():
        if v["sor szama"] != sor:
            d.write('\n')
            sor += 1
        if v["foglat"] != "foglalt":
            d.write(str(v["ar kategoria"]))
        elif v["foglat"] == "foglalt":
            d.write("x")
