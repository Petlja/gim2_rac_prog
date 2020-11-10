def trougao_brojeva_2(n):
    broj = 1
    for i in range(n + 1):
        for j in range(i):
            s = str(broj)
            print(s.rjust(4), end="")
            broj += 1
        print()

# Провера
trougao_brojeva_2(6)
