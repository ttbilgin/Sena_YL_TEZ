S1 = int(input("Birinci Sayı :"))
S2 = int(input("İkinci Sayı :"))
 try:
     sonuc = s1/s2
     print("Sonuc :",sonuc)
except ZeroDivisionError:
     print("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")