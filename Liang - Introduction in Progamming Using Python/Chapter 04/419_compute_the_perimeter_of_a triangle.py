# ================================================
# Keliling Segitiga
# ================================================

print("============================================ \n",
    "Keliling segitiga \n",
    "----------------------------------------------"
    )
sisi1, sisi2, sisi3 = eval(input("Input 3 panjang sisi segitiga : "))

# Menguji apakah sisi-sisi segitiga valid

if (sisi1 + sisi2 > sisi3 and sisi2 + sisi3 > sisi1 and sisi3 + sisi1 > sisi2):
    keliling = sisi1 + sisi2 + sisi3
    print("Keliling segitiga dengan panjang sisi",
        sisi1, ",", sisi2, ",", sisi3,
        "adalah :", keliling, "satuan panjang.")
else:
    print("Panjang sisi yang anda input tidak valid..!")

print("=============================================")