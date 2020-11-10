n = int(input())
k = int(input())
zarade = []
for i in range(n):
  x = float(input())
  zarade.append(x)

zarade.sort(reverse=True)

for i in range(k):
  print(zarade[i])
