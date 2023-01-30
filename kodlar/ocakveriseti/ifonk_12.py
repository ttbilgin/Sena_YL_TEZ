sayı=int(input("kendisine kadar olan sayıların toplamını hesaplamak istediğiniz sayıyı giriniz"))
toplam=0
for i in range(1,sayı+1):
 toplam+=i
print(toplam)