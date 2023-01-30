def faktoriyel_hesapla(sayı):
 faktoriyel=1
 if sayı==1:
 return 1
 else:
 return sayı*faktoriyel_hesapla(sayı-1)
sayı=int(input("faktoriyelini hesaplamak istediğiniz sayıyı giriniz"))
print (faktoriyel_hesapla(sayı))