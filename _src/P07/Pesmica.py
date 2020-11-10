f = open("pesmica.txt", "w")
for i in range(9):
    f.write(str(10 - i) + " little monkeys were jumping on a bed\n")
    f.write("one fell off and bumped its head.\n")
    f.write("Mommy called the doctor and the doctor said:\n")
    f.write("'No more monkeys jumping on the bed!'\n")
    f.write("\n")
# poslednja strofa
f.write("1 little monkey was jumping on a bed\n")
f.write("it fell off and bumped its head.\n")
f.write("Mommy called the doctor and the doctor said:\n")
f.write("'Put those monkeys back to bed!'\n")
f.close()
