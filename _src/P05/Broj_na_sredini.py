n = int(input())
brojevi = []
for i in range(n):
  x = float(input())
  brojevi.append(x)

brojevi.sort()

a = brojevi[n//2-1]
b = brojevi[n//2]
m = (a + b) / 2
print(m)

