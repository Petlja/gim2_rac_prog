def prvo_pojav(x, L):
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return -1

# Провера
B = ["ovo", "ono", "oko", "oro", "era", "rad", "dar", "oko", "era", "ono"]
print(prvo_pojav("oko", B))
print(prvo_pojav("iva", B))
