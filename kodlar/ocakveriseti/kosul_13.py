basariPuani=-1
vizePuani=int(input('Vize puanını giriniz: '))
finalPuani=int(input('Final puanını giriniz: '))
vizeOraniYuzde=(int(input('Vize oranını % olarak giriniz (30, 40 gibi): ')))
finalOraniYuzde=(int(input('Final oranını % olarak giriniz (70, 60 gibi): ')))
if(vizePuani>100 or vizePuani<0 or finalPuani>100 or finalPuani<0 ):
    print ('Girdiginiz vize veya final puanlarını kontrol ediniz.')
elif(vizeOraniYuzde+finalOraniYuzde)<100:
    print ('Girdiginiz vize veya % oranlarını kontrol ediniz toplam 100 olmalıdır.')
else:
    basariPuani=(vizePuani* vizeOraniYuzde/100)+(finalPuani* finalOraniYuzde/100)
if(basariPuani>=0):
    print('Başarı puanı: ', basariPuani )
if(basariPuani>= 80 and basariPuani <= 100):
    print('Başarı notu : A')
elif(basariPuani>= 70 and basariPuani <80):
    print('Başarı notu : B')
elif(basariPuani>= 60 and basariPuani <70):
    print('Başarı notu : C')
elif(basariPuani>= 50 and basariPuani <60):
    print('Başarı notu : D')
elif(basariPuani< 50 ):
    print('Başarı notu : F')