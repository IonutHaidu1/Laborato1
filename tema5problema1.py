
dosar = []
numar_referinta=0
def cauta_document(dosar, numar_referinta):
    pozitie =0
    numar_iteratii = 0
    lungimelistadocument = len(dosar)
    for i in range (lungimelistadocument):
        numar_iteratii += 1
        if dosar[i] == numar_referinta:
            pozitie=i
            break

    if pozitie == numar_iteratii - 1:
            print(f"Documentul cu numărul de referință {numar_referinta} a fost găsit pe poziția {pozitie} după {numar_iteratii} documente verificate.")
    else:
            print(f"Documentul cu numărul de referință {numar_referinta} nu a fost găsit în dosar. Total documente verificate: {numar_iteratii}.")


cauta_document([], 10)









