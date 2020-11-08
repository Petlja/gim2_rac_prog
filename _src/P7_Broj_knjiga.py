f = open("Iliad.txt", "r")
br_knjiga = 0
for red in f:
    if red[:4] == "BOOK":
        br_knjiga += 1
f.close()
print("Homerova Ilijada ima", br_knjiga, "knjiga(e)")
