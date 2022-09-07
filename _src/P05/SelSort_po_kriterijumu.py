def selection_sort_by(k, L):    # sada imamo još jedan argument (k), za kolonu po kojoj sortiramo
    n = len(L)
    if n <= 1: return
    for i in range (n-1):
        m = i
        for j in range(i+1,n):
            if L[j][k] < L[m][k]: m = j   # ovde poredimo vrednosti na k-tom mestu u redu L[j] i L[m]
        L[i], L[m] = L[m], L[i]           # ukoliko je uslov ispunjen zamenjujemo cele redove tabele

def ispisi_razred(L):           # druga funkcija je samo za ispisivanje tabele
    for red in L:
        for x in red:
            s = str(x).rjust(10)  # rjust služi samo da ispis formatira na 10 karaktera
            print(s, end="")      # end="" znači da posle štampanja kurzor ne ide novi red već nastavlja u istom
        print()

# provera
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

print("Razred sortiran po visini:")
selection_sort_by(4, razred)
ispisi_razred(razred)

print("Razred sortiran po polu:")
selection_sort_by(1, razred)
ispisi_razred(razred)