# =========================================
# Tabel Konversi Kg ke Pound
# -----------------------------------------

print("======================================== \n",
    "Tabel Konversi Kg ke Pound \n",
    "-------------------------------------------"
    )

print(
    "==================================================== \n",
    " | ", "No.  "," | ", "Kg   ", "   | ", "Pon", "       | \n",
    "--------------------------------------------------------"
    )

kilogram = 1
nomor = 1


while nomor < 100:
    pound = 2.2 * kilogram
    
    print(
    "  | ", nomor, "    | ", kilogram, "     | ", pound, "      | "
    )

    nomor += 1
    kilogram = 2 * nomor - 1 # rumus barisan bilangan ganjil
