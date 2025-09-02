abc = "abcdefghijklmnopqrstuvwxyz "

uzenet = "helloworld"
kulcs = "abcdefgijkl"

rejtjel = ""

for i in range(len(uzenet)):
    uzenet_karakter = uzenet[i]
    kulcs_karakter = kulcs[i]
    hely_uzenet = abc.index(uzenet_karakter)
    hely_kulcs = abc.index(kulcs_karakter)
    kod = (hely_uzenet + hely_kulcs) % 27
    rejtjel = abc[kod]
print(rejtjel)