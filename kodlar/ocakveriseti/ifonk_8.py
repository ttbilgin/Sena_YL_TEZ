faktoriyel=1
sayı=int(input("faktoriyelini hesaplamak istediginiz sayıyı giriniz"))
if sayı>=0:
    for i in range(1,sayı+1):
        faktoriyel*=i
print (faktoriyel)
