# sortira niz od većih ka manjim vrednostima
def selection_sort_reversed(L):
    n = len(L)
    if n <= 1: return
    for i in range (n-1):
        m = i
        for j in range(i+1,n):
            # u narednom redu je znak poredjenja okrenut!
            if L[j] > L[m]: m = j
        L[i], L[m] = L[m], L[i]

n = int(input())
zarade = []
for i in range(n):
  x = float(input())
  zarade.append(x)

selection_sort_reversed(zarade)

for i in range(n):
  print(zarade[i])
