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

# ne znamo koja devojcica je najvisa, pa stavljamo prazan string u ime
ime = ""

# ne znamo nista o njenoj visini, pa stavljamo vrednost koja je manja od svake razumne vrednosti
visina = 0

for ucenik in razred:
    if ucenik[1] == "ž" and ucenik[4] > visina:
        visina = ucenik[4]
        ime = ucenik[0]
print("Najvisa devojcica je", ime)
