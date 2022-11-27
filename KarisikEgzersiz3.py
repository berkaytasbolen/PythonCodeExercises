# Kullanicidan aldiginiz bir sayinin mukemmel olup olmadigini bulmaya calisin.

# Bir sayinin kendi haric bolenlerinin toplami kendine esitse bu sayiya "mukemmel sayi" denir. ornek olarak, 6 mukemmel bir sayidir. (1 + 2 + 3 = 6)


Sayi = int(input("Sayiyi Giriniz: "))
i = 1
toplam = 0
while(i<Sayi):
    if (Sayi % i == 0):
        toplam += i
    i += 1

if (toplam == Sayi):
     print(Sayi,"mukemmel bir sayidir.")
else:
     print(Sayi,"mukemmel bir sayi degildir.")






# Kullanicidan aldiginiz bir sayinin "Armstrong" sayisi olup olmadigini bulmaya calisin.

# ornek olarak, Bir sayi eger 4 basamakli ise ve olusturan rakamlardan herbirinin 4. kuvvetinin toplami( 3 basamakli sayilar icin 3.kuvveti ) o sayiya esitse bu sayiya "Armstrong" sayisi denir.

# ornek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4




sayi = input("Sayi:")
basamak_sayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

gecici_sayi = sayi

while (gecici_sayi > 0):
    basamak = gecici_sayi % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayi //= 10
    

if (toplam == sayi):
    print(sayi,"bir armstrong sayisidir.")
else:
    print(sayi,"bir armstrong sayisi degildir.")






# 1'den 10'kadar olan sayilarla ekrana carpim tablosu bastirmaya calisin.

    


for i in range(1,11):
    print("*************************************************")
    
    for j in range(1,11):
        
        print("{} x {} = {}".format(i,j,i*j))








# Her bir while dongusunde kullanicidan bir sayi alin ve kullanicinin girdigi sayilari "toplam" isimli bir degiskene ekleyin. Kullanici "q" tusuna bastigi zaman donguyu sonlandirin ve ekrana "toplam degiskenini" bastirin.

        
toplam = 0

while True:
    
    sayi = input("Sayi:")
    
    if (sayi == "q"):
        break
    sayi = int(sayi)
    
    toplam += sayi
    
print("Girdiginiz Sayilarin Toplami:",toplam)










# 1'den 100'e kadar olan sayilardan sadece 3'e bolunen sayilari ekrana bastirin. Bu islemi continue ile yapmaya calisin.



for i in range(1,101):
    
    if (i % 3 != 0):
        continue
        print(i)




