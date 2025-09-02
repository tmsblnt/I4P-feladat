# I4P feladat
Duális képzés
# Rejtjelező algoritmus

## 1 Titkosítás menete
- Üzenet és kulcs karaktereinek számait összeadjuk.  
- Ha nagyobb, mint 26 → osztás maradéka 27-tel.  
- Így kapjuk a rejtjel karaktereit.  

## 2 Fejtés menete
1. Vegyük a titkosított üzenet (rejtjel) és a kulcs azonos pozíciójú karaktereit.  
2. Kérjük le mindkettő számértékét az `abc` listából:  
   - `hely_rejtjel = abc.index(rejtjel_karakter)`  
   - `hely_kulcs = abc.index(kulcs_karakter)`  
3. Vonjuk ki a kulcs számát a rejtjel számából, majd vegyük a maradékot 27-tel és ezáltal megkapjuk az eredeti üzenetet 