sppTahun0 = 10000

print("---------------------------------------------")

for i in range(1,11):
    sppTahuni = sppTahun0 * (1.05) ** i # rumus compounding interest 5%/tahun
    print("SPP tahun ke-", format(i, "2d"), "adalah : USD.", format(sppTahuni,"3.2f"))
    
print("----------------------------------------------")

totalBiayaKuliah = sppTahuni * 4
print("Total biaya kuliah 10 tahun kemudian adalah : \n USD.", format(totalBiayaKuliah, "4.2f"))
print("\n (dengan asumsi kuliah selama 4 tahun)")