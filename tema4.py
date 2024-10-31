import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []

#nu afisa ca si lista, afiseaza ca string cu join
#unstring=""
#print (unstring.join(progres))
unstring=""

while incercari_ramase:
    print("Introduceti o litera")
    print(unstring.join(progres))

    litera=input()
    if not litera.isalpha():
        print("Introduceti o litera!!!")
    else:
       continue
    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if litera == cuvant_de_ghicit[i]:
                pozitielitera = i
                progres[pozitielitera]=litera

    else:
        print ("Litera este gresita")
        litere_incercate.extend(litera)
        print (f"Literele gresite pe care le-ai incercat sunt: {litere_incercate}")
    incercari_ramase = incercari_ramase - 1




