dosar = []



def cauta_document(dosar, numar_referinta):
    numar_iteratii = 0
    lungimelistadocument = len(dosar)
    for i in range (lungimelistadocument):
        if dosar[i] == numar_referinta:
            i == numar_referinta
            return i
        numar_iteratii += 1
    if i == numar_referinta:
            print(f"Documentul cu numărul de referință {numar_referinta} a fost găsit pe poziția {i} după {numar_iteratii} documente verificate.")
    else:
            print(f"Documentul cu numărul de referință {numar_referinta} nu a fost găsit în dosar. Total documente verificate: {numar_iteratii}.")


cauta_document([101, 202, 303, 404, 505, 606, 707, 808, 909], 404)




