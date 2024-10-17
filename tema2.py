articol = (" Studenții cazați în căminele Politehnica București (UNSTPB) au fost lăsați fără apă caldă de o săptămână, potrivit surselor Edupedu. "
           "Neregula vine după ce săptămâna trecută peste conductele de apă s-a surpat o stradă din apropiere, în Sectorul 6, scrie Edupedu.ro. ")
primaparte = articol [:len(articol)//2]
adouaparte = articol [len(articol)//2:]
majuscule1 = primaparte.upper()
spatiigoale = majuscule1[1:-1]
invers2=adouaparte[::-1]
eliminasemne=invers2.replace("."," ")
print(eliminasemne)