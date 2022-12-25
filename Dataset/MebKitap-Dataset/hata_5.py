while True:
x = input("Bir sayı girin: ")
if not x:
break
     y = 1/float(x)
except ValueError:
print("Geçersiz sayı")
continue
except ZeroDivisionError:
     print("Sıfıra bölme")
     continue
print(y)