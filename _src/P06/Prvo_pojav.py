def prvo_pojav(x, L):
    i = -1
    for y in L:
        i += 1
        if y == x: return i
    return -1

# Провера
B = ["ovo", "ono", "oko", "oro", "era", "rad", "dar", "oko", "era", "ono"]
print(prvo_pojav("oko", B))
print(prvo_pojav("iva", B))
