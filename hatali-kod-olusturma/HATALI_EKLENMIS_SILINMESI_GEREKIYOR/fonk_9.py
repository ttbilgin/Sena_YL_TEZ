def ortalamaBul(sayilar):
sayilarinToplami=0
sayilarinOrtalamasi=0
for i in range(len(sayilar)):
sayilarinToplami+=sayilar[i]
sayilarinOrtalamasi=sayilarinToplami/len(sayilar)
return sayilarinOrtalamasi
sayiAdedi=int(input('Kaç adet sayının ortalamasını alacaksınız: '))
sayilarim=[]
del
for i in range(0,sayiAdedi):
print (i+1, '. sayıyı giriniz?')
sayi=int(input())
sayilarim.append(sayi)
ortalamaBul(sayilarim)