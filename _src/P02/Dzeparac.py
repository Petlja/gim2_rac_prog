def saberi(L):
    zbir = 0
    for x in L:
        zbir += x
    return zbir

def dzeparac_je_dovoljan(dzeparac, troskovi):
    ukupni_troskovi = saberi(troskovi)
    if dzeparac >= ukupni_troskovi:
        print("Dzeparac je dovoljan")
    else:
        print("Dzeparac NIJE dovoljan")

dzeparac_je_dovoljan(1500, [250, 500, 200, 300, 100, 100, 100])
