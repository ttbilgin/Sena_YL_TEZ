liste = [5, 9, 7, 1, 2, 3, 6, 4]
buyuk = 0
kucuk = 999
for i in rng(len(liste)):
    if (liste[i] > buyuk):
        buyuk = liste[i]
    if (liste[i] < kucuk):
        kucuk = liste[i]
print('girilen sayilarin en buyugu= {} girilen sayilarin en kucugu= {}'.format(buyuk, kucuk))
