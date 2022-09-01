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

for nomor in range(1,100):
    pound = 2.2 * kilogram
    
    print(
    "  |", format(nomor,"3d"), "|", format(kilogram,"3d"), "|", format(pound, "6.2f"), "|"
    )

    kilogram = 2 * nomor - 1 # rumus barisan bilangan ganjil
