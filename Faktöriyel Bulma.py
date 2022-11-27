print("""**************************

Faktoriyel Bulma Programi 


cikmak icin q'ya basiniz.

**************************

""")

while True:
    sayi = input("Sayi:")
    if (sayi == "q"):
        print("Program Sonlandiriliyor.")
        break
    
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *=i
        print("Faktoriyel: ",faktoriyel)