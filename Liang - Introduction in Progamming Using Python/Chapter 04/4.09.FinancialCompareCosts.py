# =====================================
# Menentukan paket Sembako Termurah
# =====================================

beratPaket1, hargaPerPaket1 = eval(input("Input berat paket 1 (dalam Kg) dengan harga per paket 1 : "))
hargaPaket1 = beratPaket1 * hargaPerPaket1

beratPaket2, hargaPerPaket2 = eval(input("Input berat paket 2 (dalam Kg) dengan harga per paket 2 : "))
hargaPaket2 = beratPaket2 * hargaPerPaket2

if hargaPaket1 < hargaPaket2:
    print("Harga Paket 1 lebih murah..!")
elif hargaPaket2 < hargaPaket1:
    print("Harga paket 2 lebih murah...!")
elif hargaPaket1 == hargaPaket2:
    print("Harga paket 1 sama dengan paket 2...!")
else:
    print("Anda belum menginput berat paket dan harga per paket dengan benar..!!")