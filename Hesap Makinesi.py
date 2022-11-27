
print("""***************************
Hesap Makinesi Programi

Islemler:

1. Toplama Islemi
2. Cikarma Islemi
3. Carpma Islemi
4. Bolme Islemi

***************************""")

a = int(input("Birinci Sayiyi Giriniz:"))
b = int(input("Ikinci Sayiyi Giriniz:"))
islem = input("Islemi Giriniz:")
if islem == "1":
    print("{} ile {}'nin toplaminin sonucu {}'dir.".format(a,b,a+b))
elif islem == "2":
    print("{} ile {}'nin farkinin sonucu {}'dir.".format(a,b,a-b))
elif islem == "3":
    print("{} ile {}'nin Carpiminin sonucu {}'dir.".format(a,b,a*b))
elif islem == "4":
    print("{} ile {}'nin bolumunun sonucu {}'dir.".format(a,b,a/b))
else:
    print("GeCersiz Islem!")
