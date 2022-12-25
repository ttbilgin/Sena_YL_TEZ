asal_sayı=[2]
for sayı in range (3,1001):
    for bolen_sayı in range (2,sayı):
        sayı_asalmı=False
        if sayı % bolen_sayı==0:
            sayı_asalmı=True
            break
    if sayı_asalmı==False:
        asal_sayı.append(sayı)
veri=" "
for i in asal_sayı:
    veri+=str(i) # veri=veri+str(i)
    veri+=" "
dosya=open ("asalsayı.txt","w")
dosya.write(veri)
dosya.close()