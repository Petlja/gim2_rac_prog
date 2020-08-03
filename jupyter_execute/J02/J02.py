ocene = [2, 4, 5, 3, 5]

ocene

predmeti = ["matematika", "srpski", "likovno", "istorija", "fizicko"]

predmeti

len(predmeti)

godine = [1000,  1500, 1650, 1750, 1804, 1850, 1900, 1930, 1950, 1960, 1974, 1980, 1987, 1999, 2011, 2020, 2023, 2030, 2037, 2045, 2055, 2100]
ljudi  = [0.275, 0.45, 0.5,  0.7,  1,    1.2,  1.6,  2,    2.55, 3,    4,    4.5,  5,    6,    7,    7.8,  8,    8.5,  9,    9.5,  10,   11.2]

import matplotlib.pyplot as plt

plt.plot(godine, ljudi)
plt.show()
plt.close()

plt.plot(godine, ljudi)
plt.title("Broj stanovnika na Zemlji")
plt.show()
plt.close()

plt.plot(godine, ljudi)
plt.title("Broj stanovnika na Zemlji")
plt.ylabel("(milijarde)")
plt.show()
plt.close()