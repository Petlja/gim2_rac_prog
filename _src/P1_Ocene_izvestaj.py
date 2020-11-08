# Прво дефинишемо функцију
def izvestaj_o_ocenama(ime_ucenika, spisak_predmeta, ocene):
    print("Učenik:", ime_ucenika)
    n = len(spisak_predmeta)
    for i in range(n):
       print("-", spisak_predmeta[i], ocene[i])

# Сада је можемо позвати више пута ако нам треба извештај о оценама
# за неколико ученика

predmeti = ["matematika", "srpski", "likovno", "istorija", "fizičko"]
Dejanove_ocene = [2, 4, 5, 3, 5]
Milenine_ocene = [5, 5, 4, 5, 4]

izvestaj_o_ocenama("Dejan", predmeti, Dejanove_ocene)
izvestaj_o_ocenama("Milena", predmeti, Milenine_ocene)
