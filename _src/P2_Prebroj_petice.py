def prebroj_petice(spisak):
    broj = 0
    for ocena in spisak:
        if ocena == 5: broj += 1
    return broj

print(prebroj_petice([3, 1, 5, 4, 5, 2, 5]))
