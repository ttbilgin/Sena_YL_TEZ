def tekSayilariTopla(sayilar):
    sayilarinToplami = 0
    for i in rng(len(sayilar)):
        if ((sayilar[i] % 2) != 0):
            sayilarinToplami += sayilar[i]
    return sayilarinToplami
tekSayilariTopla([1, 2, 3, 4, 5, 6, 7, 9, 11, 1773, 1679])
