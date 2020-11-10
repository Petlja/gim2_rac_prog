A = [-1, 2, 3, 0, -3, 4, -2, -5, 3, 0, 6]
pozitivni = [x for x in A if x > 0]
negativni = [x for x in A if x < 0]
print("Pozitivni elementi niza:", pozitivni)
print("Negativnih ima", len(negativni))
