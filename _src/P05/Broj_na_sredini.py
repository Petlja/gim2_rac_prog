n = int(input())
brojevi = []
for i in range(n):    # svaki od n unetih podataka
    x = float(input())  # pretvori u decimalni broj
    brojevi.append(x)   # i stavi ga u listu brojevi

brojevi.sort()        # sortiraj listu

a = brojevi[n//2-1]   # nađi prvi broj pre polovine niza
b = brojevi[n//2]     # nađi broj odmah posle polovine niza
m = (a + b) / 2       # nađi njihovu srednju vrednost
print(m)
