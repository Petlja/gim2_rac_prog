def prebroj_podstr(p, s):
    broj = 0
    n = len(p)
    for i in range(len(s) - n + 1):
        if p == s[i:i+n]:
            broj += 1
    return broj

# провера
print(prebroj_podstr("bana", "oprobana torta od banana"))
