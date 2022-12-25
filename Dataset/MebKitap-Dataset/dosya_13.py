def rezervasyon_yap():
     rezervasyon_kapasitesi=50
     dosya=open("rezervasyon.txt","r+", encoding="utf-8")
     rezervasyonlar=dosya.readlines()
     mecut_rezervasyon=len(rezervasyonlar)
     if rezervasyon_kapasitesi-mecut_rezervasyon >0 :
         print(rezervasyon_kapasitesi-mecut_rezervasyon,"adet daha rezervasyon yapabiliriz")
         yeni_rezervasyon=input("rezervasyon bilgilerini araya virgül girerek giriniz")
         dosya.write("\n"+yeni_rezervasyon )
         print("rezervasyon numaranız =",mecut_rezervasyon+1,end="")
         print("rezervasyon bilgileriniz : ",yeni_rezervasyon)
         print("razervasyonunuz başarıya tamamlanmıştır.")
     else:
         print("rezervasyon kapasitemiz dolmuştur.")
     dosya.close()
print("rezervasyon ekranına hoş geldiniz")
rezervasyon_yap()