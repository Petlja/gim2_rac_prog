s = input("Unesi string")
br_otvorenih = 0
br_zatvorenih = 0
for x in s:
    if x == "(": br_otvorenih += 1
    if x == ")": br_zatvorenih += 1
if br_otvorenih == br_zatvorenih:
    print("isti je broj otvorenih i zatvorenih zagrada")
else:
    print("nije isti broj otvorenih i zatvorenih zagrada")
