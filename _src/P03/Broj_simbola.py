print("Utvrdjujemo koliko puta se neki simbol javlja u unetom stringu")
c = input("Unesi simbol: ")
s = input("Unesi string: ")
broj = 0
for x in s:
    if x == c:
        broj += 1
print("Simbol", c, "se u unetom stringu javlja", broj, "puta")
