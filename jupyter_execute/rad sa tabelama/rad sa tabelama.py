podaci = [["Ana",     "ž", 13, 46, 160],
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

podaci[4]

sum = 0
for dete in podaci:
    sum += dete[4]
sum/len(podaci)

import pandas as pd

tabela = pd.DataFrame(podaci)

tabela

tabela = pd.DataFrame(podaci)
tabela.columns=["Ime", "Pol", "Starost", "Masa", "Visina"]
tabela

tabela["Ime"]

tabela["Visina"]

tabela.columns

tabela["Visina"].min()

tabela["Starost"].max()

tabela["Visina"].mean()

tabela["Visina"].median()

import pandas as pd
podaci = [["Ana",     "ž", 13, 46, 160],
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
tabela = pd.DataFrame(podaci)
tabela.columns=["Ime", "Pol", "Starost", "Masa", "Visina"]
tabela1=tabela.set_index("Ime")

tabela

tabela1

tabela1["Ime"]

tabela1.index

tabela1.loc["Dejan"]

tabela1.loc["Dejan":"Zoran"]

tabela1.loc["Dejan", "Visina"]

tabela1.loc["Dejan":"Zoran", "Masa":"Visina"]

razred = [["Ana",     5, 3, 5, 2, 4, 5],
          ["Bojan",   5, 5, 5, 5, 5, 5],
          ["Vlada",   4, 5, 3, 4, 5, 4],
          ["Gordana", 5, 5, 5, 5, 5, 5],
          ["Dejan",   3, 4, 2, 3, 3, 4],
          ["Đorđe",   4, 5, 3, 4, 5, 4],
          ["Elena",   3, 3, 3, 4, 2, 3],
          ["Žaklina", 5, 5, 4, 5, 4, 5],
          ["Zoran",   4, 5, 4, 4, 3, 5],
          ["Ivana",   2, 2, 2, 2, 2, 5],
          ["Jasna",   3, 4, 5, 4, 5, 5]]

ocene = pd.DataFrame(razred)
ocene.columns=["Ime", "Informatika", "Engleski", "Matematika", "Fizika", "Hemija", "Likovno"]
ocene1 = ocene.set_index("Ime")
ocene1

for predmet in ocene1.columns:
    print(predmet, "->", round(ocene1[predmet].mean(), 2))

print("Đorđe ima sledeće ocene:")
print(ocene1.loc["Đorđe"])
print("Prosek njegovih ocena je:", 
      round(ocene1.loc["Đorđe"].mean(), 2))

for ucenik in ocene1.index:
    print(ucenik, "->", round(ocene1.loc[ucenik].mean(), 2))

ocene1

ocene2 = ocene1.T

ocene2

ocene1.index

ocene1.columns

ocene2.index

ocene2.columns

for predmet in ocene1.columns:
    print(predmet, "->", round(ocene1[predmet].mean(), 2))

for ucenik in ocene2.columns:
    print(ucenik, "->", round(ocene2[ucenik].mean(), 2))