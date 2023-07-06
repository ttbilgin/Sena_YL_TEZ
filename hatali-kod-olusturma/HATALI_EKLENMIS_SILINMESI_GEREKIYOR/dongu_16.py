sesli_harfler = "aeiou"
sessiz_harfler = "bcdfghjklmnprsştvyz"
sesliler=""
sessizler=""
pass
a = input("bir metin giriniz")
for i in a:
if i in sesli_harfler:
sesliler=sesliler+i
if i in sessiz_harfler:
sessizler=sessizler+i
print("sesli harfler",sesliler)
print("sessiz harfler",sessizler)