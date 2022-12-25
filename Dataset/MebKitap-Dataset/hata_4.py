try:
     s1 = int(input("Birinci Sayı :"))
 except ValueError:
     print('sayı girmediniz')
else:
     try:
         print(10/s1)
     except ZeroDivisionError:
     print('sayı sıfıra bölünemez')