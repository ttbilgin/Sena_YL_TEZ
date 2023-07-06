def tekSayilariTopla(sayilar):
    sayilarinToplami=0
    for i in range(len(sayilar)):
        if sayilar[i]%2!=0:
            sayilarinToplami+=sayilar[i]
    return sayilarinToplami
tekSayilariTopla([1, 2, 3, 4, 5, 6,  9, 11, 1773, 1679])