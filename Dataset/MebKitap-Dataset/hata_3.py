try:
    s1 = int(input("Birinci Sayı :"))
    sonuc = s1**2
    print("Sonuc :",sonuc)
except ValueError as hata:
    print('Lütfen sayı giriniz')
    print(hata)