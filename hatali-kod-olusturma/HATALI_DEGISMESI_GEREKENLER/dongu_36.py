a = nt(input('bir sayi giriniz'))
asal = 0
for i in range(2, a):
    if ((a % i) == 0):
        asal += 1
if (asal == 0):
    print('girdiginiz sayi asal')
else:
    print('girdiğiniz sayi asal degil')
