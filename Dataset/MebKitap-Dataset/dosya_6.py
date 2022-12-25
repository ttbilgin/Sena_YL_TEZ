with open("asalsayı.txt","r") as dosya :
    veri=dosya.read()
    asal_sayılar=veri.split(" ")
kontrol_sayısı=input("asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz")
if kontrol_sayısı in asal_sayılar :
    print("asal sayı")
else:
    print("asal sayı değil")
