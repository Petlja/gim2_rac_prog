def posl_pojav(x, L):
    n = len(L)
    for i in reversed(range(n)):
        if L[i] == x:
            return i
    return -1

# Провера
B = ["ovo", "ono", "oko", "oro", "era", "rad", "dar", "oko", "era", "ono"]
print(posl_pojav("oko", B))
print(posl_pojav("rad", B))
print(posl_pojav("iva", B))
