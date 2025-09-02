abc = "abcdefghijklmnopqrstuvwxyz "

uzenet = "helloworld"
kulcs = "abcdefgijkl"


# 1) Rejtjelezés
rejtjel = ""

for i in range(len(uzenet)):
    uzenet_karakter = uzenet[i]
    kulcs_karakter = kulcs[i]
    hely_uzenet = abc.index(uzenet_karakter)
    hely_kulcs = abc.index(kulcs_karakter)
    kod = (hely_uzenet + hely_kulcs) % 27
    rejtjel = rejtjel + abc[kod]
print(rejtjel)

# 2) Visszafejtés

fejtett = ""

for i in range(len(rejtjel)):
    rejtjel_karakter = rejtjel[i]
    kulcs_karakter = kulcs[i]
    hely_rejtjel = abc.index(rejtjel_karakter)
    hely_kulcs = abc.index(kulcs_karakter)
    kod = (hely_uzenet - hely_kulcs) % 27
    fejtett = fejtett + abc[kod]

print(fejtett)