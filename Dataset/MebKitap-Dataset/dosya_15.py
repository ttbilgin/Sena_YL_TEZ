def rezervasyon_sil(rezervasyon_no):
     dosya=open("rezervasyon.txt","r+",encoding="utf-8")
     rezervasyonlar=dosya.readlines()
     if rezervasyon_no <len(rezervasyonlar):
         print("rezervason bilgileriniz: ",rezervasyonlar[rezervasyon_no])
         emin_misiniz=input("kaydı silmek istediğinziden emin misiniz e/h")
         if emin_misiniz=="e" or emin_misiniz=="E":
             rezervasyonlar.pop(rezervasyon_no)
             dosya.seek(0)
             dosya.writelines(rezervasyonlar)
             dosya.close()
         print("rezervasonunuz başarıyla güncellenmişitir.")
         else:
             print("rezervasyon silme işleminiz iptal edilmişitir")
     else:
         print("hatalı bir rezervason numarası girdiniz")
print("rezervasyon silme ekranına hoşgeldiniz")
rezervasyon_no=input("lütfen rezervasyon numaranızı giriniz")
rezervasyon_sil(int(rezervasyon_no))