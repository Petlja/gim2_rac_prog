def trougao_brojeva(n):
    for i in range(n + 1):
        for j in range(i):
            s = str(j + 1)
            print(s.rjust(4), end="")
        print()

# Провера
trougao_brojeva(6)

