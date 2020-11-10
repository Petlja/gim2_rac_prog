def bubble_sort_by(k, L):
    n = len(L)
    if n <= 1: return
    zamena = True
    while zamena:
        zamena = False
        for i in range(n-1):
            # ovde poredimo vrednosti na k-tom mestu u redu L[i] i L[i+1]
            if L[i][k] > L[i+1][k]:
                zamena = True
                L[i], L[i+1] = L[i+1], L[i]
        n -= 1

def ispisi_razred(L):
    for red in L:
        for x in red:
            s = str(x).rjust(10)
            print(s, end="")
        print()

# Провера
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
bubble_sort_by(4, razred)
ispisi_razred(razred)

print("Razred sortiran po polu:")
bubble_sort_by(1, razred)
ispisi_razred(razred)
