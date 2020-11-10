# Učitavanje podataka
n = int(input("Koliko ima predmeta? "))
print("Za", n, "predmeta unesi imena i ocene")
predmeti = []
ocene = []
for i in range(n):
  ime = input("Ime "+ str(i+1) + ". predmeta: ")
  ocena = int(input("Ocena: "))
  predmeti.append(ime)
  ocene.append(ocena)

# Računanje minimuma i maksimuma
min_ocena = min(ocene)
max_ocena = max(ocene)

# Ispis predmeta iz kojih je učenih najbolje, odnosno, najlošije ocenjen
if min_ocena == max_ocena:
  print("Ti si primer konstantnog kvaliteta!")
else:
  print("Tvoji najbolje ocenjeni predmeti su:")
  for i in range(n):
    if(ocene[i] == max_ocena):
      print("-", predmeti[i])
  print("Tvoji najlošije ocenjeni predmeti su:")
  for i in range(n):
    if(ocene[i] == min_ocena):
      print("-", predmeti[i])
