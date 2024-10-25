meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
tava=[]

while len(studenti):
         student=studenti.pop(0)
         comanda=comenzi.pop(0)
         tava=tavi.pop(-1)
         print(f"{student} a comandat {comanda}")

print(tava)


