def prebroj_cifre(n):
    br_cif = 0
    while n > 0:
        br_cif += 1
        n //= 10
    return br_cif

print(prebroj_cifre(12487))
