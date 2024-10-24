meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
   #   for  i in range(0, len(studenti)):
    #    student=studenti.pop(0)
     #   comanda=comenzi.pop(0)
      #  tava=tavi.pop(-1)
       # print(f"{student} a comandat {comanda}")

student1=studenti.pop(0)
comanda1=comenzi.pop(0)
tava1=tavi.pop(0)
istoric_comenzi.append(comanda1)

print(f"{student1} a comandat {comanda1}")

student2=studenti.pop(0)
comanda2=comenzi.pop(0)
tava2=tavi.pop(0)
istoric_comenzi.append(comanda2)
print(f"{student2} a comandat {comanda2}")

student3=studenti.pop(0)
comanda3=comenzi.pop(0)
tava3=tavi.pop(0)
istoric_comenzi.append(comanda3)
print(f"{student3} a comandat {comanda3}")

student4=studenti.pop(0)
comanda4=comenzi.pop(0)
tava4=tavi.pop(0)
istoric_comenzi.append(comanda4)
print(f"{student4} a comandat {comanda4}")

student5=studenti.pop(0)
comanda5=comenzi.pop(0)
tava5=tavi.pop(0)
istoric_comenzi.append(comanda5)
print(f"{student5} a comandat {comanda5}")

print (f"{istoric_comenzi.count("guias")} portii de guias s-au cumparat")
print (f"{istoric_comenzi.count("ceafa")} portii de ceafa s-au cumparat")
print (f"{istoric_comenzi.count("papanasi")} portii de papanasi s-au cumparat")
print (f"{tavi.count("tava")}")
