import random

'''
1-100 arasinda rastgele üretilecek bir sayıyı asağı yukaı ifadeleri ile
buldurmaya calisin.
** "random modülü" icin "python random" seklinde arama yapin.
** 100 üzerinden puanlama yapin. Her soru 20 puan.
** Hak bilgisini kullanicidan alin ve her soru belirtilen can sayis1
üzerinden hesaplansin.
'''


rand = random.randint(0,100)
hp = 0
print("1: Çok Kolay\n2: Kolay \n3: Orta \n4: Zor \n5: Çok Zor")
zorluk = int(input("Zorluk seçmek için numara giriniz:"))
if zorluk == 1:
    hp = 20
    print("Seçilen Zorluk:Çok Kolay, Tahmin Hakkı : 25, Zorluk Çarpanı:3")
elif zorluk == 2:
    hp = 15
    print("Seçilen Zorluk:Kolay, Tahmin Hakkı : 15, Zorluk Çarpanı:5")
elif zorluk == 3:
    hp = 10
    print("Seçilen Zorluk:Orta, Tahmin Hakkı : 10, Zorluk Çarpanı:10")
elif zorluk == 4:
    hp = 5
    print("Seçilen Zorluk:Zor, Tahmin Hakkı : 5, Zorluk Çarpanı:15")
elif zorluk == 5:
    hp = 3
    print("Seçilen Zorluk:Çok Zor, Tahmin Hakkı:3, Zorluk Çarpanı:25")
else:
    print("Sadece 1 ve 5 arasinda sayi girebilirsiniz!")

print("0 ile 100 arasında tahmin yapın. Her yanlış tahminde hak 1 azalacaktır")

while hp > 0:
    print(f'\nKalan Tahmin Hakkı:{hp}')
    tahmin = int(input('Tahmininiz:'))
    if tahmin == rand:
        if zorluk == 1:
            puan = hp * 3
        elif zorluk == 2:
            puan = hp * 5
        elif zorluk == 3:
            puan = hp * 10
        elif zorluk == 4:
            puan = hp * 15
        elif zorluk == 5:
            puan = hp * 25
        
        print("Doğru Tahmin ettiniz!\n")
        print(f'Skor :{puan}')

        break
    elif tahmin > rand:
        print("AŞAĞI")
        hp -= 1
    else:
        print("YUKARI")
        hp -=1

    if hp == 0:
        print("HAK BİTTİ!")


