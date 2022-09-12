pokokPinjaman = eval(input("Input total pinjaman : Rp."))
jangkaWaktuPinjaman = eval(input("Input jangka waktu pinjaman (dalam satuan tahun) :"))
persenBungaPerTahun = eval(input("Input bunga pinjaman per tahun : "))

totalPengembalian = round(pokokPinjaman * (1 + persenBungaPerTahun / 100) ** jangkaWaktuPinjaman, 2)
cicilanBulanan = round(totalPengembalian / (12 * jangkaWaktuPinjaman), 2)

print("Total pengembalian : Rp.", format(totalPengembalian, ".2f"))
print("Cicilan bulanan : Rp.", format(cicilanBulanan, ".2f"))


persenBungaBulanan = persenBungaPerTahun / 1200
sisaPokok = pokokPinjaman

print("==================================================================================================")
print("|", "Bulan ke-", "|", "Bunga Bulanan", "|", "Pembayaran Pokok Pinjaman", "|", "Pokok Pinjaman", "|")
print("--------------------------------------------------------------------------------------------------")
for i in range(1, jangkaWaktuPinjaman * 12 + 1):
    nominalBungaBulanan = persenBungaBulanan * pokokPinjaman
    sisaPokokBulanan = cicilanBulanan - nominalBungaBulanan
    pokokpinjaman = pokokPinjaman - sisaPokokBulanan

    print("|", format(i, "9d"), "|", format(nominalBungaBulanan, "13.2f"), "|", format(sisaPokokBulanan, "24.2f"), "|", format(pokokPinjaman, "14.2f"))
    
print("--------------------------------------------------------------------------------------------------")