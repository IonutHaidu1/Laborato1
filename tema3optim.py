meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
casademarcat=0
limitadepret=7

while len(studenti):
         tava=tavi.pop(-1)
         student=studenti.pop(0)
         comanda=comenzi.pop(0)
         istoric_comenzi.append(comanda)
         print(f"{student} a comandat {comanda}")
print (f"S-au comandat {istoric_comenzi.count("guias")} portii de guias, {istoric_comenzi.count("ceafa")} portii de ceafa {istoric_comenzi.count("papanasi")} portii de papanasi")
print (f"Mai sunt {len(tavi)} tavi")
print (f"Mai este ceafa?{istoric_comenzi.count("ceafa")<meniu.count("ceafa")}")
print (f"Mai sunt papanasi?{istoric_comenzi.count("papanasi")<meniu.count("papanasi")}")
print (f"Mai este guias?{istoric_comenzi.count("guias")<meniu.count("guias")}")

if len(istoric_comenzi)>0:
    casademarcat=istoric_comenzi.count("guias") * 5 +istoric_comenzi.count("ceafa") * 10 + istoric_comenzi.count("papanasi") * 7
    print (f"Cantina a incasat {casademarcat} lei")
else:
    print (f"Nu au fost clienti")

for item in preturi:
    item_name=item[0]
    item_price=item[1]
    if item_price <= limitadepret:
        print(f"{item_name} costa {item_price}")
















