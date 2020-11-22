def pozicije_pozitivnih(L):
    n = len(L)
    rez = []
    for i in range(n):
        if L[i] > 0:
            rez.append(i)
    return rez

# Провера
print(pozicije_pozitivnih([3, -1, 2, 4, -6, 0, 5]))
print(pozicije_pozitivnih([-1, -2, -3]))
print(pozicije_pozitivnih([]))
