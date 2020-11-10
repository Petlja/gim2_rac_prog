def broj_reci(s):
    n = len(s)
    broj = 0
    for i in range(n-1):
        if s[i].isalpha() and not s[i+1].isalpha():
            broj += 1
    if s[n-1].isalpha():
        broj += 1
    return broj

# провера
print(broj_reci("Ovo je samo primer!"))
print(broj_reci("Proba"))
print(broj_reci("!!!!"))
