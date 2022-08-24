print("===========================================================================")
print("Tabel Pinjaman dan Pengembalian")
print("----------------------------------------------------------------------------\n")
totalPinjaman = eval(input("Input total pinjaman : "))
jangkaWaktu = eval(input("Input jangka waktu pinjaman (dalam tahun): "))
bunga = 5.000
i = 1

print("----------------------------------------------------------------------------")
print("|", "No.", "|", format("Bunga per tahun","15s"),"|",format("Cicilan per bulan", "20s"), "|", format("Total Pembayaran", "20s"), "|")
print("----------------------------------------------------------------------------")

while bunga <= 8:
    bungaDesimal = bunga / 100
    totalHutang = totalPinjaman * (1 + bungaDesimal) ** jangkaWaktu
    cicilan = totalHutang / (12 * jangkaWaktu)
    print("|", format(i,"3d"), "|", format(bunga, "15.3f"),"|", format(cicilan, "20.2f"), "|", format(totalHutang, "20.2f"), "|")
    i += 1
    bunga += 0.125

print("===========================================================================")