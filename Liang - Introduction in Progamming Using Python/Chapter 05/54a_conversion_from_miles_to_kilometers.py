# =========================================================
# Konversi Mil ke Kilometer
# =========================================================

print(
    "=================================================== \n",
    "Konversi Mil ke Kilometer \n",
    "--------------------------------------------------- \n"
    )

nomor = 1

print(
    "================= \n"
    "No.  ", "Mil   ", "Kg   ", "\n",
    "------------------"
    )

while nomor < 11:
    mil = nomor
    kilogram = 1.609 * mil
    print(
        nomor, "   ",mil, "   ",kilogram
        )
    nomor += 1

print("==========================")