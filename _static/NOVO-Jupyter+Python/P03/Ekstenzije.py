fajl = input("Unesi ime fajla: ")
ekstenzija = fajl[-4:] # uzimamo poslednja 4 simbola imena
if ekstenzija in [".txt", ".log"]:
    print("tekstualni fajl")
elif ekstenzija in [".png", ".jpg", ".bmp"]:
    print("slika")
elif ekstenzija == ".mpg":
    print("video")
elif ekstenzija == ".mp3":
    print("zvuk")
else:
    print("Ovaj format mi nije poznat")
