
print("""**********************
Kullanici GiriSi
**********************
""")

sys_nickname = "j3rkay"
sys_password = "123456"

Kullanici_adi = input("Kullanici Adi:")
sifre = input("Sifre:")

if (sys_nickname==Kullanici_adi and sys_password!=sifre):
    print("Sifreniz Hatali...")
elif (sys_nickname!=Kullanici_adi and sys_password==sifre):
    print("Kullanici Adiniz Hatali...")
elif (sys_nickname!=Kullanici_adi and sys_password!=sifre):
    print("Kullanici Adi ve Sifreniz Hatali...")
else:
    print("...GiriS BaSariyla GercekleStirildi...")