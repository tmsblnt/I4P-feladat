abc = "abcdefghijklmnopqrstuvwxyz "

# 1. feladat

# 1) Rejtjelezés
def titkosit(uzenet,kulcs):
    rejtjel = ""
    for i in range(len(uzenet)):
        uzenet_karakter = uzenet[i]
        kulcs_karakter = kulcs[i]
        hely_uzenet = abc.index(uzenet_karakter)
        hely_kulcs = abc.index(kulcs_karakter)
        kod = (hely_uzenet + hely_kulcs) % 27
        rejtjel = rejtjel + abc[kod]
    return rejtjel

# 2) Visszafejtés

def fejtes(rejtjel, kulcs):
    fejtett = ""
    for i in range(len(rejtjel)):
        rejtjel_karakter = rejtjel[i]
        kulcs_karakter = kulcs[i]
        hely_rejtjel = abc.index(rejtjel_karakter)
        hely_kulcs = abc.index(kulcs_karakter)
        kod = (hely_rejtjel - hely_kulcs) % 27
        fejtett = fejtett + abc[kod]
    return fejtett

print(titkosit("helloworld","abcdefgijkl") + "\n" + fejtes("helloworld","abcdefgijkl"))

# 2. feladat
szavak = []
with open("words.txt", "r", encoding="UTF-8") as f:
    for szo in f:
        szo = szo.strip()
        if szo:
            szavak.append(szo)

if "curiosity" in szavak:
    print("A curiosity szó benne van a listában.")
    