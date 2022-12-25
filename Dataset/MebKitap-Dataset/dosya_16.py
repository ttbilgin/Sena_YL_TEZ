dosya=open("sayı.txt","r")
sayılar=dosya.readlines()
dosya.close()
# sayıları string olarak aldık sayıya dönüştürüp sıralayıp tekrardan stringe
dönüştüreceğiz
for i in range(len(sayılar)):
     sayılar[i]=int (sayılar[i])
     sayılar.sort()
for i in range(len(sayılar)):
     sayılar[i]=str(sayılar[i])+"\n"
dosya=open("sıralı.txt","w")
dosya.writelines(sayılar)
dosya.close()