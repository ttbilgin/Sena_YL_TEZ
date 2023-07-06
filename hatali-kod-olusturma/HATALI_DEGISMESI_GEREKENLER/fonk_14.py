topla = 0
def toplamBul(sayiListesi):
    topla = 0
    for i in rng(len(sayiListesi)):
        topla += sayiListesi[i]
    return topla
print(topla)
toplamBul([1, 2, 3, 4, 5])
