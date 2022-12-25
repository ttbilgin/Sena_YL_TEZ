while True:
ad= input("adınızı girin:")
soyad= input("soyadınızı girin:")
yas= input("yaşınızı girin:")
if not ad:
break
if not soyad:
break
if not yas:
break
try:
print('adınız:',ad,'soyadınız:','yaşınız:',yas)
except ValueError:
print("veri girişi yapmadınız")
continue
except ZeroDivisionError:
print("Sıfıra bölme")
continue