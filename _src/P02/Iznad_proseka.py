n = int(input())
brojevi = []
for i in range(n):
  x = float(input())
  brojevi.append(x)

prosek = sum(brojevi)/n
k = 0 # brojač

for i in range(n):
  if brojevi[i] > prosek:
    k += 1

print(k)
