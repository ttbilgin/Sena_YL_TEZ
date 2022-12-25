import turtle
kalem=turtle.Turtle()
mesafe=int(input("çizgi mesafesini
giriniz"))
donus_açısı=int(input("dönüş açısını
giriniz"))
kalem.forward(mesafe)
kalem.right(donus_açısı)
kalem.forward(mesafe)
turtle.done()
