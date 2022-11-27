
# # Kullanicidan alinan 3 sayiyi carparak ekrana yazdirma.

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

carpim = a * b * c

print("Birinci Sayi: {}\nIkinci Sayi: {}\nucuncu Sayi: {}\ncarpim Sonucu: {}\n".format(a,b,c,carpim))



# # Beden Kitle Endexi Bulma

a = int(input("Kilonuz:"))
b = float(input("Boyunuz(m):"))

c = a/(b*b)

print("Kilonuz: {}\nBoyunuz {}\nBeden Kitle Endeksiniz {}\n".format(a,b,c))



# # Bir Aracin Kilometrede Ne kadar yaktigi ve kac km gittigi bilgisini ali ve ucret cikar

a = float(input("Gidilen Yol(Km):"))
b = float(input("Km basina yaktigi fiyat:"))
c = a*b

print("\n")

print("Gidilen Mesafe: {} km\nKm basina ucret: {}\n**Odemeniz Gereken Toplam ucret**\n {}\n".format(a,b,c))



# # Kullanici Kaydi Sistemi

a = str(input("Ad:"))
b = str(input("Soyad:"))
c = int(input("Telefon Numarasi:"))
print("\n")

print("Kaydiniz Tamamlaniyor...\nKaydiniz Basariyla Tamamnlandi.")

print("\n")

print("Adiniz: {}\nSoyadiniz:{}\nNumaraniz:\n".format(a,b,c))
print("**Aramiza Hosgeldiniz**\n")



# # Kullanicidan Iki Deger Isteyip Bu Degerleri birbirleriyle Degistir.

a = input("Ilk Deger:")
b = input("Ikinci Deger:")

print("Yeni Ilk Degeriniz: {}\nYeni Ikinci Degeriniz: {}\n".format(b,a))



# # Kullanicidan bir dik ucgenin dik olan iki kenarini(a,b) alin ve hipotenus uzunlugunu bulmaya calisin.

a = int(input("Ilk Kenar Uzunlugunu Giriniz:"))
b = int(input("Ikinci Kenar Uzunlugunu Giriniz:"))
c = (a**2+b**2)**0.5
print("\n")
print("Ilk Kenar: {}\nIkinci Kenar: {}\nHipotenus:{}\n".format(a,b,c))
