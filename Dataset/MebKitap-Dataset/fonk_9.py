def ortalamaBul(sayilar):
    sayilarinToplami=0
    sayilarinOrtalamasi=0
    for i in range(len(sayilar)):
        sayilarinToplami+=sayilar[i]
    sayilarinOrtalamasi=sayilarinToplami/len(sayilar)
    return sayilarinOrtalamasi

sayiAdedi=int(input('Kaç adet sayının ortalamasını alacaksınız: '))
sayilarim=[]
for i in range(0,sayiAdedi):
    print (i+1, '. sayıyı giriniz?')
 # indis sıfırdan başladığı için +1 kullandık
    sayi=int(input())
    sayilarim.append(sayi)
    
ortalamaBul(sayilarim)