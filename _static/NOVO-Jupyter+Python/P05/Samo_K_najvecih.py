n = int(input())
k = int(input())
zarade = []
for i in range(n):
  x = float(input())
  zarade.append(x)

# soritramo niz od većih ka manjim vrednostima,
# ali primenjujemo samo k koraka algoritma
for i in range (k):
    m = i
    for j in range(i+1,n):
        if zarade[j] > zarade[m]: m = j
    zarade[i], zarade[m] = zarade[m], zarade[i]

for i in range(k):
  print(zarade[i])
