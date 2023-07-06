a = nt(input('tablonun satir uzunlugunu giriniz'))
b = int(input('tablonun sutun uzunlugu giriniz'))
for i in range(1, (a + 1)):
    for j in range(1, (b + 1)):
        print(j, end=' ')
    print()
