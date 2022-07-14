# ======================================================
# Menentukan Posisi Titik Terhadap Lingkaran
# ======================================================

print("================================================= \n",
    "Menentukan Posisi Titik Terhadap Lingkaran \n",
    "---------------------------------------------------",
    )

# Pengguna menginput jari-jari dan titik pusat
jari2 = eval(input("Input jari-jari lingkaran : "))
absisTitikPusat, ordinatTitikPusat = eval(input("Input titik pusat lingkaran : "))

# Periksa apakah jari-jari yang diinput valid?
if jari2 > 0: #jari2 harus lebih dari 0
    if (absisTitikPusat > 0 and ordinatTitikPusat > 0):
        print("Persamaan lingkaran :",
            "( x -", absisTitikPusat,") ^ 2", " + ( y -", ordinatTitikPusat, ") ^ 2 = ", jari2 ** 2
            )
    elif (absisTitikPusat < 0 and ordinatTitikPusat < 0):
        print("Persamaan lingkaran :",
            "( x +", abs(absisTitikPusat),") ^ 2", " + ( y +", abs(ordinatTitikPusat), ") ^ 2 = ", jari2 ** 2
            )
    elif (absisTitikPusat < 0 and ordinatTitikPusat > 0):
        print("Persamaan lingkaran :",
            "( x +", abs(absisTitikPusat),") ^ 2", " + ( y -", ordinatTitikPusat, ") ^ 2 = ", jari2 ** 2
            )
    elif (absisTitikPusat > 0 and ordinatTitikPusat < 0):
        print("Persamaan lingkaran :",
            "( x -", absisTitikPusat,") ^ 2", " + ( y +", abs(ordinatTitikPusat), ") ^ 2 = ", jari2 ** 2
            )
    elif (absisTitikPusat == 0 and ordinatTitikPusat == 0):
        print("Persamaan lingkaran :",
            "x ^ 2 + y ^ 2 = ", jari2 ** 2
            )
    elif (absisTitikPusat < 0 and ordinatTitikPusat == 0):
        print("Persamaan lingkaran :",
            "( x +", abs(absisTitikPusat),") ^ 2", " + y ^ 2 =", jari2 ** 2
            )
    elif (absisTitikPusat > 0 and ordinatTitikPusat == 0):
        print("Persamaan lingkaran :",
            "( x -", absisTitikPusat,") ^ 2", " + y ^ 2 =", jari2 ** 2
            )
    elif (absisTitikPusat == 0 and ordinatTitikPusat < 0):
        print("Persamaan lingkaran :",
            "x ^ 2", " + ( y +", abs(ordinatTitikPusat), ") ^ 2 = ", jari2 ** 2
            )
    elif (absisTitikPusat == 0 and ordinatTitikPusat > 0):
        print("Persamaan lingkaran :",
            "x ^ 2", " + ( y -", ordinatTitikPusat, ") ^ 2 = ", jari2 ** 2
            )
else:
    print("Jari-jari harus lebih dari 0.")

# Pengguna menginput titik lain
absisTitik, ordinatTitik = eval(input("Input titik lain :"))

# Hitung jarak titik sembarang dengan titik pusat
jarakTitik = ((absisTitik - absisTitikPusat) ** 2 + (ordinatTitik - ordinatTitikPusat) ** 2) ** (1/2)

# Membandingkan jarak titik dengan jari-jari
if jarakTitik == jari2:
    print(
        "Titik",
        "(", absisTitik, ",", ordinatTitik, ")",
        "terletak pada lingkaran."
    )
elif jarakTitik < jari2:
   print(
        "Titik",
        "(", absisTitik, ",", ordinatTitik, ")",
        "terletak di dalam lingkaran."
    )
else:
   print(
        "Titik",
        "(", absisTitik, ",", ordinatTitik, ")",
        "terletak di luar lingkaran."
    )
print("===================================================================================") 