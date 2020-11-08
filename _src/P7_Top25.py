f = open("Top25YouTubers.csv", "r")
br_vid = 0
naj_kanal = ""
prvi_red = True
for red in f:
    if prvi_red:
        prvi_red = False
    else:
        s = red.split(",")
        if int(s[3]) > br_vid:
            br_vid = int(s[3])
            naj_kanal = s[2]
f.close()
print("Najvise videa je objavio kanal", naj_kanal)
