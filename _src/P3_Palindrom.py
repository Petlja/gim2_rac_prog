s = input("Unesi string: ")
novi = ""
obrnut = ""
for x in s.lower():
    if x.isalpha():
        novi = novi + x
        obrnut = x + obrnut
if novi == obrnut:
    print("jeste palindrom")
else:
    print("nije palindrom")
