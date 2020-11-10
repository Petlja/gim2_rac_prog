f = open("Iliad.txt", "r")
br_ahil = 0
br_hektor = 0
for red in f:
    br_ahil += red.count("Achilles")
    br_hektor += red.count("Hector")
f.close()
print("Ahil se pominje", br_ahil, "puta")
print("Hektor se pominje", br_hektor, "puta")
