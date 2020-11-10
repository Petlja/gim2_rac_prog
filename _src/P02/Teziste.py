n = int(input())
x_koord = []
y_koord = []
for i in range(n):
  tacka = input()
  koord = tacka.split()
  x = float(koord[0])
  y = float(koord[1])
  x_koord.append(x)
  y_koord.append(y)

T_x = sum(x_koord) / n
T_y = sum(y_koord) / n

print(T_x, T_y)

