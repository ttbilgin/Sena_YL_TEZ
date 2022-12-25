import turtle
def desen_çiz (kenar_uzunlugu=50,ic_kenar=3,tur_sayısı=3):
    if(tur_sayısı <1 or ic_kenar<3):
        print("hatalı veri girdiniz")
    else:
        kalem=turtle.Turtle()
        for i in range (tur_sayısı):
            for j in range (ic_kenar):
                kalem.forward(kenar_uzunlugu)
                kalem.left(360/ic_kenar)
            kalem.left(360/tur_sayısı)
desen_çiz()
desen_çiz(60,4,5)
desen_çiz(70,6,10)
turtle.done()