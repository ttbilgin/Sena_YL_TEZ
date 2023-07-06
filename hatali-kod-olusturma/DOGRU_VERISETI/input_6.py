on_mesaj="Sayın "
mesaj_sonu=" nisan dönemi faturaınız: "
abone_no=input("abone numaranız")
tuketim=input("tuketim miktarı")
tuketim_tutari=int(tuketim)*4.0
mesaj=on_mesaj+abone_no+mesaj_sonu+tuketim+" tl dir."
print(mesaj)
