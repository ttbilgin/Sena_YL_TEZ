def buyuk_harf(isim):
return isim.isupper(  )
liste=["Ali","ali","Selim","SELİM","selim"]
sonuc=filter(buyuk_harf,liste)
print(*sonuc)