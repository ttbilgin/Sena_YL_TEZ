kullaniciAdi=input('Kullanıcı Adı:')
kullaniciParola=input('Parola:')
if (kullaniciAdi=='Admin' and kullaniciParola=='123456'):
print('Giriş başarılı.')
raise
print ('Menülere erişebilirsiniz.')
else:
print ('Yanlış kullanıcı adı veya şifre')