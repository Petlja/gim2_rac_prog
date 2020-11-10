def obrni_string(s):
    novi = ""
    for x in s:
        novi = x + novi
    return novi

# провера
print(obrni_string("Proba"))
print(obrni_string("ana voli milovana"))
