print("""**************************

Atm Makinesine Hos Geldiniz.

Islemler;

1. Bakiye Sorgulama
2. Para Yatirma
3. Para cekme

Kart iadesi icin 'x' e basiniz.

**************************

""")

bakiye = 1000

while True:
    islem = input("Islemi Seciniz:")

    if(islem == "x"):
        print("Tekrar bekleriz...")
    elif(islem == "1"):
        print("Bakiyeniz {} TL'dir.".format(bakiye))
    
    elif(islem == "2"):
        miktar = int(input("Miktari Giriniz:"))
        bakiye += miktar
    
    elif(islem == "3"):
        miktar = int(input("Miktari Giriniz:"))
        
        if (bakiye - miktar < 0):
            print("Bakiye Yetersiz...")
            continue
        bakiye -= miktar


    else:
        print("Gecersiz Islem...")