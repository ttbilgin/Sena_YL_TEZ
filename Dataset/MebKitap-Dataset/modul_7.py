import random
sayılar=[]
for i in range (50):
 sayı=str(random.randint(0,1000))+"\n"
 sayılar.append(sayı)
dosya=open("sayı.txt","w")
dosya.writelines(sayılar)
dosya.close()