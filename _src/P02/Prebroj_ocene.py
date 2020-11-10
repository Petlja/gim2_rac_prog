def prebroj_ocene(spisak, n):
    broj = 0
    for ocena in spisak:
        if ocena == n: broj += 1
    return broj

print(prebroj_ocene([3, 1, 5, 4, 5, 2, 5, 1, 2], 1))
