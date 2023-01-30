def faktoriyel_hesapla(sayı):
 faktoriyel=1
 if sayı>=0:
 for i in range(1,sayı+1):
 faktoriyel*=i
 return faktoriyel
sayı=int(input("faktoriyelini hesaplamak istediğiniz sayıyı giriniz"))
print (faktoriyel_hesapla(sayı))