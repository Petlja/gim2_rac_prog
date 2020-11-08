dzeparac = float(input())
troskovi = 0
unos = input()
while unos != "stop":
    x = float(unos)
    troskovi += x
    unos = input()
if dzeparac >= troskovi:
    print("Dovoljan je")
else:
    print("Nije dovoljan")

