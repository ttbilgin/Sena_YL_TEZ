def faktoriyelAl(sayi):
    sonuc=1
    if (sayi==0 or sayi==1):
        sonuc=1
    elif sayi>1:
        for i in range(1, sayi+1, 1):
            sonuc*=i
    else: sonuc=-1 #hatalı bir işlem olduğunu anlamak için -1 değerini veriyoruz
    return sonuc

sonucumuz=faktoriyelAl(5)
#fonksiyonu bir değişkene atayabiliyoruz.
if sonucumuz!=-1: # bir hata olup olmadığını kontrol edelim
    print(sonucumuz)
else:print('Bir hata oluştu')