def max_5_slova(L):
    return [s for s in L if len(s) <= 5]

# Провера
niz = ["abrakadabra", "ali", "popokatepetl", "tata", "jabuka", "ja", "biologija", "te", "infomratika", "banana", "volim"]
print(max_5_slova(niz))
