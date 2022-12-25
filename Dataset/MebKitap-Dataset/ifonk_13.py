def topla(sayı):
 if sayı==1:
 return 1
 else:
 return sayı+topla(sayı-1)
sayı=int(input("kendisine kadar olan sayıların toplamını hesaplamak istediğiniz sayıyı giriniz"))
print(topla(sayı))