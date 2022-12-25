dosya=open("deneme.txt","r")
# dosyamızı for döngüsü ile okuyoruz
for veri in dosya:
    print(veri)
#imlecin nerede olduğunu ekrana yazdırıyoruz
print(dosya.tell())
# imleci 10. bayta taşıyoruz
dosya.seek(10)
#imlecin bulunduğu yerden 20 bayt veri okuyoruz
print(dosya.read(20))
#imlecin nerede olduğunu görüntülüyoruz
print(dosya.tell())
dosya.close()