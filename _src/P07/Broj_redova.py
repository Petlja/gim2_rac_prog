f = open("Iliad.txt", "r")
br_redova = 0
for red in f:
    br_redova += 1
f.close()
print("Datoteka Iliad.txt ima", br_redova, "redova")
