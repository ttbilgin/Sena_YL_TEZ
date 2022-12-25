def rezerevasyon_yap():
    rezervasyon_bilgi=input("rezervasyon bilgilerinizi giriniz")
    veri=rezervasyon_bilgi+","
    dosya=open("rezervasyon.txt","a")
    dosya.write(veri)
    dosya.close()
def rezerevasyon_kontrol() :
    rezervasyon_bilgi=input("rezervasyon bilgilerinizi giriniz")
    with open("rezervasyon.txt","r") as dosya:
        veri=dosya.read()
        rezervasyonlar=veri.split(",")
        if rezervasyon_bilgi in rezervasyonlar:
            print("rezervasyonunuz bulunmaktadır.")
        else:
            print("rezervasyon kaydınız yoktur.")
while True:
    islem=input("rezervasyon yapmak için 1 : kontrol için 2 programı kapatmak için 3 e basınız")
    if islem=="1" :
        rezerevasyon_yap()
    elif islem =="2":
        rezerevasyon_kontrol()
    else:
        break