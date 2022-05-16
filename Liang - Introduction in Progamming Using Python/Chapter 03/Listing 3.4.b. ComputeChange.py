# ================================================
# Menentukan Banyak Lembar Dolar dan Koin
# ================================================

# 1. Input jumlah besaran uang (dalam US Dollar)
besaranDolar = eval(input("Input besaran uang dalam US dolar (contoh. USD.11.57) : USD."))

# 2. Kalikan besaran dolar dengan bilangan 100
besaranSen = besaranDolar * 100

# 3. Tentukan jumlah lembar 1 dolaran
lembarDolaran = int(besaranSen // 100)
sisaDolar = besaranSen % 100

# 4. Tentukan jumlah koin Quarter
koinQuarter = int(sisaDolar // 25)
sisaQuarter = sisaDolar % 25

# 5. Tentukan jumlah koin Dime
koinDime = int(sisaQuarter // 10)
sisaDime = sisaQuarter % 10

# 6. Tentukan jumlah koin Nickel
koinNickel = int(sisaDime // 5)
sisaNickel = sisaDime % 5

# 7. Tentukan jumlah koin Penny
koinPenny = int(sisaNickel)

# 8. Tampilkan hasil
print(
        "Uang sebesar USD.", besaranDolar, "terdiri dari : \n",
        "\t", lembarDolaran, "lembar 1 dolaran.\n",
        "\t", koinQuarter,"koin Quarter.\n",
        "\t", koinDime, "koin Dime.\n",
        "\t", koinNickel,"koin Nickel.\n",
        "\t", koinPenny, "koin Penny."
)
