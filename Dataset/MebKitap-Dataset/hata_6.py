try:
s1 = int(input("Birinci Sayi :"))
s2 = int(input("ikinci Sayi :"))
s3 = int(input("üçüncü Sayi :"))
sonuc = s1+s2+s3
print("Sonuc :",sonuc)
except ZeroDivisionError:
print("lütfen sıfrıdan farklı bir sayı giriniz¦")
except ValueError:
print('lütfen sayısal bir değer giriniz')
