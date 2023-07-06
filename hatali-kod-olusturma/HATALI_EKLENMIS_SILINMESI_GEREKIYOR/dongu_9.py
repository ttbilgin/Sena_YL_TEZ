sayi = 45
sayac = 0
print("1-100 arasi bir sayi tuttum tahmin et")
await
while 1==1:
sayac += 1
cevap=int(input("1-100 arasi bir sayi girin:"))
if cevap>sayi:
print("daha kucuk bir sayi girmelisin")
elif cevap<sayi:
print("daha buyuk bir sayi girmelisin")
else:
print("tebrikler tuttugum sayiyi bildin")
break
print("tebrikler {} seferde sayiyi bulabildin".format(sayac))