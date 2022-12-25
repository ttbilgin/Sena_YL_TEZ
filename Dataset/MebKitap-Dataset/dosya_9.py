dosya=open("deneme.txt","r+")
dosya.seek(20)
#dosyada 20. bayta gittik
dosya.write("20. bayttan itibaren yazdık")
#20. bayttan sonraki verilerin üzerine yazdık
print(dosya.tell())
# imlecin 47. bayta geldiğini öğreneceğiz
#burda dosyadan okuma yaparsak 47. bayttan sonrası okunacak
print(dosya.read())
# listemizdeki verileri en sona yazıyoruz
liste=["1","2","3","4"]
#listedeki veriler string olmazsa hata alırız.
dosya.writelines (liste)