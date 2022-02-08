fiyat = 10
baslangicEn = int(input("En: "))
bitisEn = int(input("En: "))

toplamSatir = (((bitisEn-baslangicEn)/10)+1)*4
toplamSatir = int(toplamSatir)


baslangicSku = 1
bitisSku = toplamSatir
print("Toplam Satır ", toplamSatir)
while baslangicSku <= toplamSatir:
    for pile in [1, 2, 2.5, 3]:


        if pile != 3 :
            print("En: ",  baslangicEn, "Pile :", pile, "Satır: ", baslangicSku, "Fiyat: ", ((((baslangicEn)/100)*pile)+20/100)*fiyat )
            baslangicSku += 1
        elif pile == 3 :
            print("En: ",  baslangicEn, "Pile :", pile, "Satır: ", baslangicSku, "Fiyat: ", ((baslangicEn/100)*pile)*fiyat )
            baslangicSku +=1
    baslangicEn += 10
