def izdvoj_pozitivne(L):
    rez = []
    for x in L:
        if x > 0:
            rez.append(x)
    return rez

# Провера
print(izdvoj_pozitivne([3, -1, 2, 4, -6, 0, 5]))
print(izdvoj_pozitivne([-1, -2, -3]))
print(izdvoj_pozitivne([]))
