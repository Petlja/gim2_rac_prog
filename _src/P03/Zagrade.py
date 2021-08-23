s = input("Unesi string")
br_jemanje = 0
br_jevece = 0
for x in s:
    if x == "<": br_jemanje += 1
    if x == ">": br_jevece += 1
if br_jemanje == br_jevece:
    print("isti je broj znakova < и >")
else:
    print("nije isti broj znakova < и >")
