for i in range(10):
    for j in range(10):
        s = str((i + 1)*(j + 1))
        print(s.rjust(4), end="")
    print()
