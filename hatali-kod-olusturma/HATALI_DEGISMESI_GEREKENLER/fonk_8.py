def faktoriyelAl(sayi):
    sonuc = 1
    if ((sayi == 0) or (sayi == 1)):
        sonuc = 1
    elif (sayi > 1):
        for i in range(1, (sayi + 1), 1):
            sonuc *= i
    else:
        sonuc = (- 1)
    return sonuc
sonucumuz = faktoriyelAl(5)
if (sonucumuz != (- 1)):
    print(sonucumuz)
else:
    print('Bir hata oluştu')
