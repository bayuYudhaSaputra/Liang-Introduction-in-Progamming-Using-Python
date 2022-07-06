# ==========================================================
# Menyatakan bulan dan Tahun
# ==========================================================

bulan = eval(input("Input bulan ke- (misal bulan ke-1): "))
tahun = eval(input("Input tahun : "))

if bulan == 1:
    print(
        "Bulan Januari", tahun,
        "mempunyai 31 hari."
        )
elif bulan == 2:
    print(
        "Bulan Februari", tahun,
        "mempunyai 28 hari."
        )
elif bulan == 3:
    print(
        "Bulan Maret", tahun,
        "mempunyai 31 hari."
        )
elif bulan == 4:
    print(
        "Bulan April", tahun,
        "mempunyai 30 hari."
        )
elif bulan == 5:
    print(
        "Bulan Mei", tahun,
        "mempunyai 31 hari."
        )
elif bulan == 6:
    print(
        "Bulan Juni", tahun,
        "mempunyai 30 hari."
        )
elif bulan == 7:
    print(
        "Bulan Juli", tahun,
        "mempunyai 31 hari."
        )
elif bulan == 8:
    print(
        "Bulan Agustus", tahun,
        "mempunyai 31 hari."
        )
elif bulan == 9:
    print(
        "Bulan September", tahun,
        "mempunyai 30 hari."
        )
elif bulan == 10:
    print(
        "Bulan Oktober", tahun,
        "mempunyai 31 hari."
        )
elif bulan == 11:
    print(
        "Bulan November", tahun,
        "mempunyai 30 hari."
        )
elif bulan == 12:
    print(
        "Bulan Desember", tahun,
        "mempunyai 31 hari."
        )
else:
    print("Input bulan ke- 1 hingga 12.")