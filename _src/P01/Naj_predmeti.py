n = int(input("Koliko ima predmeta? "))         # unos broja predmeta
print("Za", n, "predmeta unesi imena i ocene")
predmeti = []                                   # liste predmeti i ocene su prazne na početku
ocene = []
for i in range(n):                                  # za svaki predmet 
  ime = input("Ime "+ str(i+1) + ". predmeta: ")    # prvo unosimo ime
  ocena = int(input("Ocena: "))                     # pa onda ocenu koju pretvaramo u integer
  predmeti.append(ime)                 # listi predmeti dodajemo novo ime
  ocene.append(ocena)                  # listi ocene dodajemo novu ocenu

# računanje minimuma i maksimuma
min_ocena = min(ocene)
max_ocena = max(ocene)

# ispis predmeta iz kojih je učenih najbolje, odnosno, najlošije ocenjen
if min_ocena == max_ocena:                      # ako su najveća i najmanja ocena iste
  print("Ti si primer konstantnog kvaliteta!")  # ispiši ovu poruku
else:                                           # u protivnom
  print("Tvoji najbolje ocenjeni predmeti su:") # ispiši liste najbolje i nalošije ocenjenih predmeta
  for i in range(n):
    if(ocene[i] == max_ocena):
      print("-", predmeti[i])
  print("Tvoji najlošije ocenjeni predmeti su:")
  for i in range(n):
    if(ocene[i] == min_ocena):
      print("-", predmeti[i])