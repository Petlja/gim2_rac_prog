for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                if 1000*a + 100*b + 10*c + d == (a + b + c + d)**3:
                    print(1000*a + 100*b + 10*c + d)
