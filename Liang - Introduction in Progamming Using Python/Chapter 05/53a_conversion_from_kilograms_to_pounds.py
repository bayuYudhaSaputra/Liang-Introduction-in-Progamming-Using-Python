# =========================================
# Tabel Konversi Kg ke Pound
# -----------------------------------------

print(" ============================= \n",
    "Tabel Konversi Kg ke Pound \n",
    "--------------------------"
    )

print(
    " ======================= \n",
    " |", format("No.","3s"),"|", format("Kg ","3s"), "|", format("Pon","6s"), "|\n",
    "-----------------------"
    )

kilogram = 1
nomor = 1


while nomor < 100:
    pound = 2.2 * kilogram
    
    print(
    "  |", format(nomor,"3"), "|", format(kilogram,"3"), "|", format(pound, "6.2f"), "|"
    )

    nomor += 1
    kilogram = 2 * nomor - 1 # rumus barisan bilangan ganjil
