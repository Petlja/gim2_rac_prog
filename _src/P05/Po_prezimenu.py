def ispisi_razred(L):
    for red in L:
        for x in red:
            s = str(x).rjust(10)
            print(s, end="")
        print()

def po_prezimenu(L):
    ???

# Провера
razred = [
    ["Dejan", "Dejanović", 3, 4, 5, 4, 5],
    ["Mara", "Marić", 4, 5, 5, 4, 2],
    ["Miloš", "Milošević", 2, 5, 4, 3, 3],
    ["Petar", "Marković", 5, 4, 5, 5, 5]
]

po_prezimenu(razred)
ispisi_razred(razred)
