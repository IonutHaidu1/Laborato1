import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []
unstring=""
numaratoare =0

while incercari_ramase:
    print("Introduceti o litera")
    print(unstring.join(progres))

    litera=input()
    if not litera.isalpha():
        print("Introduceti o litera!!!")
    if litera in litere_incercate:
        print (f"Ai mai incercat aceasta litera")

    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        numaratoare += 1
        for i in range(len(cuvant_de_ghicit)):
            if litera == cuvant_de_ghicit[i]:
                pozitielitera = i
                progres[pozitielitera] = litera
                litere_incercate.append(litera)

    else:
        print ("Litera este gresita")
        litere_incercate.append(litera)
        print (f"Literele pe care le-ai incercat pana acum sunt: {litere_incercate}")
        incercari_ramase = incercari_ramase - 1
        print (f"Mai ai {incercari_ramase} incercari")
    if numaratoare== len(cuvant_de_ghicit):
      break

if numaratoare == len(cuvant_de_ghicit):
        print(f"Felicitari! Ai gasit cuvantul!")
else:
        print (f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}")



