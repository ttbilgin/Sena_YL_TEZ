import functools
sayı=int(input("faktöriyelini hesaplamak istediğiniz sayıyı giriniz"))
liste=[i for i in range(1,sayı+1)]
print (functools.reduce(lambda x,y :x*y,liste))