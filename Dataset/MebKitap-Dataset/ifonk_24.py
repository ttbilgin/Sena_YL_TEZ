#müşteriler listesi müşteri no ile bakiye miktarı
musteriler= [[1, 12], [2, 600], [ 3, 500], [4,150]]
sonuc = filter(lambda x: (x[1] > 149),musteriler )
print(*sonuc)