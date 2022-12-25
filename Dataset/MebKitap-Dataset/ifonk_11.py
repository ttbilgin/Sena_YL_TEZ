def fibonacci(n):
 if n <= 2:
 return 1
 else:
 return fibonacci(n-1) + fibonacci(n-2)
sayı=int(input("hesaplanmasını istediğiniz fibonacci terim sayısını giriniz"))
print(fibonacci(sayı))