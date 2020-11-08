def pozicije_pozitivnih(L):
    i = -1
    rez = []
    for x in L:
        i += 1
        if x > 0:
            rez.append(i)
    return rez

# Провера
print(pozicije_pozitivnih([3, -1, 2, 4, -6, 0, 5]))
print(pozicije_pozitivnih([-1, -2, -3]))
print(pozicije_pozitivnih([]))
