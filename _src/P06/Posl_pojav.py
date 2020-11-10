def posl_pojav(x, L):
    i = -1
    n = -1
    for y in L:
        i += 1
        if y == x: n = i
    return n

# Провера
B = ["ovo", "ono", "oko", "oro", "era", "rad", "dar", "oko", "era", "ono"]
print(posl_pojav("oko", B))
print(posl_pojav("rad", B))
print(posl_pojav("iva", B))
