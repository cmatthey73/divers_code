
note = input("La note : ")

if note == "":
    raise Exception("Falscher Aufruf: Bitte übergeben Sie eine Zahl!")

note = int(note)

if note > 6 or note < 1:
    raise Exception("Falscher Wert: Die Note muss einen Wert zwischen 1..6 haben!")

txt = "Der Test ist bestanden" if note >=4 else "Der Test ist nicht bestanden"

if note == 6 :
    res = "Note 6 : sehr gut"
elif note >= 5 :
    res = "Note 5+ : gut"
elif note >= 4 :
    res = "Note 4+ : genugend"
else :
    res = "ungenugend"

print(txt)
print(res)


