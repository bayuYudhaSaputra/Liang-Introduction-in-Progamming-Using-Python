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
    " ========================= \n"
    " |", "No.","|", format("Mil","5s"), "|",format("Kg","5s"), "|", "\n",
    "-------------------------"
    )

while nomor < 11:
    mil = nomor
    kilogram = 1.609 * mil
    print(
        " |",format(nomor,"3d"), "|",format(mil, "5.2f"), "|",format(kilogram, "5.2f"),"|"
        )
    nomor += 1

print("==========================")