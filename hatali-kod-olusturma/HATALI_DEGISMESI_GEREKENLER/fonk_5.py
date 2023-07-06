def asalMi(sayi):
    sayac = 2
    while (sayac <= int((sayi / 2))):
        if ((sayi % sayac) == 0):
            return False
        sayac += 1
    return True
asalMi(113)
