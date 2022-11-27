# Problem 1
# Kullanicidan alinan boy ve kilo degerlerine gore beden kitle indeksini hesaplayin ve su kurallara gore ekrana su yazilari yazdirin.

#  Beden Kitle Indeksi: Kilo / Boy(m) *  Boy(m)

#  BKI 18.5'un altindaysa -------> Zayif

#  BKI 18.5 ile 25 arasindaysa ------> Normal

#  BKI 25 ile 30 arasindaysa --------> Fazla Kilolu

#  BKI 30'un ustundeyse -------------> Obez

boy = float(input("Boyunuzu Giriniz(m):"))
kilo = float(input("Kilonuzu Giriniz:"))
kitle_indeksi = kilo / (boy*boy)

print("Beden Kitle Indeksiniz:{}\n".format(kitle_indeksi))
if kitle_indeksi<18.5:
    print("Zayif")
elif 18.5<kitle_indeksi<25:
    print("Normal")
elif 25<kitle_indeksi<30:
    print("Fazla Kilolu")
elif kitle_indeksi>30:
    print("Obez")




#Problem 2
# Kullanicidan 3 tane sayi alin ve en buyuk sayiyi ekrana yazdirin.

a = int(input("Ilk Sayiyi GIiriniz:"))
b = int(input("Ikinci Sayiyi Giriniz:"))
c = int(input("ucuncu Sayiyi GIiriniz:"))

if (a>=b and a>=c):
    print("En buyuk sayi {}'dir.".format(a))
elif (b>=a and b>=c):
    print("En buyuk sayi {}'dir.".format(b))
elif (c>=a and c>=b):
    print("En buyuk sayi {}'dir.".format(c))






# Problem 3
# Kullanicinin girdigi vize1,vize2,final notlarina notlarina gore harf notunu hesaplayin.

#     Vize1 toplam notun %30'una etki edecek.

#     Vize2 toplam notun %30'una etki edecek.

#     Final toplam notun %40'ina etki edecek.


#     Toplam Not >=  90 -----> AA

#     Toplam Not >=  85 -----> BA

#     Toplam Not >=  80 -----> BB

#     Toplam Not >=  75 -----> CB

#     Toplam Not >=  70 -----> CC

#     Toplam Not >=  65 -----> DC

#     Toplam Not >=  60 -----> DD

#     Toplam Not >=  55 -----> FD

#     Toplam Not <  55 -----> FF



a = int(input("Birinci Vize Notunuz:"))
b= int(input("Ikinci Vize Notunuz:"))
c= int(input("Final Notunuz:"))

toplam= (a*30)/100 + (b*30)/100 + ((c*40)/100)

if toplam >= 90:
    print("AA")
elif toplam>= 85:
    print("BA")
elif toplam>=80:
    print("BB")
elif toplam>=75:
    print("CB")
elif toplam>=70:
    print("CC")
elif toplam>=65:
    print("DC")
elif toplam>=60:
    print("DD")
elif toplam>=55:
    print("FD")
elif toplam>=50:
    print("FF")
else:
    print("Kaldiniz.")






# simdi de geometrik sekil hesaplama islemi yapalim. Ilk olarak kullanicidan ucgenin mi dortgenin mi tipini bulmak istedigini sorun.

# Eger kullanici "Dortgen" cevabini verirse , 4 tane kenar isteyip bu dortgenin kare mi , dikdortgen mi yoksa siradan bir dortgen mi oldugunu bulmaya calisin.

# Eger kullanici "ucgen" cevabini verirse , 3 tane kenar isteyip bu ucgenin ikizkenar mi , eskenar mi yoksa siradan bir ucgen mi oldugunu bulmaya calisin. Eger verilen kenarlar bir ucgen belirtmiyorsa, ekrana "ucgen belirtmiyor" seklinde bir yazi yazin.

# abs() ---- mutlak deger alma komutudur.



sekil =  input("Hangi seklin tipini ogrenmek istiyorsunuz?")

if (sekil == "Dortgen"):
    print("Lutfen kenarlari sirayla giriniz.") 
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))
   
    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdortgen")
    else:
        print("Dortgen")
        
    

if (sekil == "ucgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))

    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eskenar ucgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Ikizkenar ucgen....")
        else:
            print("cesitkenar ucgen...")
    else:
        print("ucgen belirtmiyor...")

            
else:
    print("Gecersiz sekil...")
