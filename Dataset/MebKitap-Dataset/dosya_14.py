def rezervasyon_güncelle(rezervasyon_no):
     dosya=open("rezervasyon.txt","r+",encoding="utf-8")
     rezervasyonlar=dosya.readlines()
     if rezervasyon_no <len(rezervasyonlar):
         print("rezervason bilgileriniz: ",rezervasyonlar[rezervasyon_no])
         güncelleme=input(" lütfen rezervasyon güncelleme bilgilerini giriniz")
         rezervasyonlar[rezervasyon_no]=güncelleme+"\n"
         print(" güncel rezervason bilgileriniz: ",rezervasyonlar[rezervasyon_no])
         dosya.seek(0)
         dosya.writelines(rezervasyonlar)
         dosya.close()
         print("rezervasonunuz başarıyla güncellenmişitir.")
     else:
         print("hatalı bir rezervason numarası girdiniz")
print("rezervasyon güncelleme ekranına hoş geldiniz")
rezervasyon_no=input("lütfen rezervasyon numaranızı giriniz")
rezervasyon_güncelle (int(rezervasyon_no))