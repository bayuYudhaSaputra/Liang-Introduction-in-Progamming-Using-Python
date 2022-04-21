# =======================================================================================
# Split bilangan 4 digit
# ---------------------------------------------------------------------------------------
# Langkah 1.  Input bilangan 4 digit
bilangan4Digit = eval(input("Input bilangan 4 digit (mis. 3125) :"))

# Langkah 2.  Ambil digit satuan dengan rumus :
digitSatuan = bilangan4Digit % 10

# Langkah 3.  Operasikan bilangan ribuan dengan 10
#               menggunakan operasi pembagian integer dengan rumus :
bilangan3Digit = bilangan4Digit // 10

# Langkah 4.  Ambil digit puluhan dengan rumus : 
digitPuluhan = bilangan3Digit % 10

# Langkah 5.  Operasikan bilangan ratusan dengan 10
#               menggunakan operasi pembagian integer dengan rumus :
bilangan2Digit = bilangan3Digit // 10

# Langkah 6.  Ambil digit ratusan dengan rumus :
digitRatusan = bilangan2Digit % 10

# Langkah 7.  Ambil digit ribuan menggunakan operasi pembagian integer dengan rumus :
digitRibuan = bilangan2Digit // 10

# Langkah 8.  Tampilkan digit ribuan
print(digitRibuan)

# Langkah 9.  Tampilkan digit ratusan
print(digitRatusan)

# Langkah 10. Tampilkan digit puluhan
print(digitPuluhan)

# Langkah 11. Tampilkan digit satuan
print(digitSatuan)

# =======================================================================================