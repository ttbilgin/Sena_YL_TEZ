sesli_harfler=["a","e","i","o","u"]
rakamlar="1234567890"
ozel_harf=["@","!","&","?"]
ozel_harf_sayisi,rakam_sayisi,sesli_sayisi=0,0,0
kelime=input("lutfen incelemek icin bir metin giriniz: ")
for harf in kelime:
    if harf in sesli_harfler:
        sesli_sayisi+=1
    if harf in rakamlar:
        rakam_sayisi+=1
    if harf in ozel_harf:
        ozel_harf_sayisi+=1
print("girdiginiz metinde {} adet sesli harf {} adet rakam ve {} adet ozel karakter bulunmaktadir. ".format(sesli_sayisi,rakam_sayisi,ozel_harf_sayisi) )