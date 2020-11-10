f = open("Iliad.txt", "r")
ceo_tekst = f.read()
f.close()

print("Ahil se pominje", ceo_tekst.count("Achilles"), "puta")
print("Hektor se pominje", ceo_tekst.count("Hector"), "puta")
