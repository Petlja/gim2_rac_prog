for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if 1000*a + 100*b + 10*c + d == (a + b + c + d)**3:
                    print(1000*a + 100*b + 10*c + d)
