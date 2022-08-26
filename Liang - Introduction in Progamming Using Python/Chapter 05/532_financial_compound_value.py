print("\n=====================================================")
import sys
cicilanPerBulan = eval(input("Berapa nominal uang yang disisihkan per bulan? Rp."))
bunga = eval(input("Berapa persen bunga yang didapat per bulan?"))
jangkaWaktu = eval(input("Berapa bulan jangka waktu yang dibutuhkan?"))

print("-------------------------------------------------------")

if cicilanPerBulan <= 0 or jangkaWaktu <= 0 or bunga <= 0:
    print("Jumlah nominal uang yang disisihkan, bunga dan jangka waktu harus diinput bilangan lebih dari 0")
    exit()
else:
    bungaPerBulan = bunga / 1200
    pengaliBunga = (1 + bungaPerBulan)
    jumlahTabungan = 0
    for i in range(1, jangkaWaktu + 1):
        cicilanPerBulan *= pengaliBunga
        jumlahTabungan += cicilanPerBulan
        jumlahTabunganPlusBunga = jumlahTabungan * pengaliBunga

    print("Jumlah tabungan setelah", jangkaWaktu,
        "bulan adalah Rp", format(jumlahTabunganPlusBunga, ".2f")
    )

print("\n=====================================================")    