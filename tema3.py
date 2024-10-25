meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
casa_de_marcat = 0;

student1=studenti.pop(0)
comanda1=comenzi.pop(0)
tava1=tavi.pop(-1)
istoric_comenzi.append(comanda1)

print(f"{student1} a comandat {comanda1}")

student2=studenti.pop(0)
comanda2=comenzi.pop(0)
tava2=tavi.pop(-1)
istoric_comenzi.append(comanda2)
print(f"{student2} a comandat {comanda2}")

student3=studenti.pop(0)
comanda3=comenzi.pop(0)
tava3=tavi.pop(-1)
istoric_comenzi.append(comanda3)
print(f"{student3} a comandat {comanda3}")

student4=studenti.pop(0)
comanda4=comenzi.pop(0)
tava4=tavi.pop(-1)
istoric_comenzi.append(comanda4)
print(f"{student4} a comandat {comanda4}")

student5=studenti.pop(0)
comanda5=comenzi.pop(0)
tava5=tavi.pop(-1)
istoric_comenzi.append(comanda5)
print(f"{student5} a comandat {comanda5}\n")


print (f"S-au cumparat:{istoric_comenzi.count("guias")} portii de guias,  "
       f"{istoric_comenzi.count("ceafa")} portii de ceafa,  "
       f"{istoric_comenzi.count("papanasi")} portii de papanasi." "\n"
        f"Au ramas: {tavi.count("tava")} tavi." )
casa_de_marcat = (istoric_comenzi.count("ceafa") * preturi[1][1]) + (istoric_comenzi.count("papanasi") * preturi[0][1]) + (istoric_comenzi.count("guias") * preturi[2][1])
print (f"Au mai ramas portii de guias? : {istoric_comenzi.count('guias') < meniu.count('guias')}")
print (f"Au mai ramas portii de ceafa? : {istoric_comenzi.count('ceafa') < meniu.count('ceafa')}")
print (f"Au mai ramas portii de papanasi? : {istoric_comenzi.count('papanasi') < meniu.count('papanasi')} \n")
print (f"Cantina a incasat:{casa_de_marcat} lei.")
print (f"Produse care costa cel mult 7 lei: {preturi[0]} {preturi[2]}")





