try:
     s1 = int(input("Birinci Sayı :"))
     s2 = int(input("İkinci Sayı :"))
     sonuc = s1/s2
     print("Sonuc :",sonuc)
except ZeroDivisionError:
     print("Lütfen ikinci sayıya sıfırdan farklı bir değer girin…")
except ValueError:
     print('Lütfen sayısal bir karakter girin..')
except:
     print("Beklenmeyen bir hata oluştu")