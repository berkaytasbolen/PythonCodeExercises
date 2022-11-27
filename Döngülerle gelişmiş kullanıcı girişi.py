print("""
*************************
Kullanici Girisi Programi
*************************
""")

sys_kullanici_adi = "Berkay"

sys_parola = "123456"
giris_hakki = 3


while True:
    kullanici_adi = input("Kullanici Adi:")
    parola = input("Parola:")
    if (kullanici_adi != sys_kullanici_adi and  parola == sys_parola):
        print("Kullanici Adi Hatali...")
        giris_hakki -= 1
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatali...")
        giris_hakki -= 1 
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanici Adi ve Parola Hatali...")
        giris_hakki -= 1 
    else:
        print("Sisteme basariyla giris yapildi...")
        break
    if (giris_hakki == 0):
        print("Giris Hakkiniz Bitti...")
        break