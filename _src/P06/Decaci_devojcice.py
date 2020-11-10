def ispisi_grupu(L):
    for red in L:
        for x in red:
            s = str(x).rjust(10)
            print(s, end="")
        print()


razred = [["Ana",     "ž", 13, 46, 160],
          ["Bojan",   "m", 14, 52, 165],
          ["Vlada",   "m", 13, 47, 157],
          ["Gordana", "ž", 15, 54, 165],
          ["Dejan",   "m", 15, 56, 163],
          ["Đorđe",   "m", 13, 45, 159],
          ["Elena",   "ž", 14, 49, 161],
          ["Žaklina", "ž", 15, 52, 164],
          ["Zoran",   "m", 15, 57, 167],
          ["Ivana",   "ž", 13, 45, 158],
          ["Jasna",   "ž", 14, 51, 162]]

decaci = [ucenik for ucenik in razred if ucenik[1] == "m"]
devojcice_13_14 = [ucenik for ucenik in razred if ucenik[1] == "ž" and (ucenik[2] == 13 or ucenik[2] == 14)]

print("Dečaci:")
ispisi_grupu(decaci)

print("Devojčice sa 13 ili 14 godina:")
ispisi_grupu(devojcice_13_14)
