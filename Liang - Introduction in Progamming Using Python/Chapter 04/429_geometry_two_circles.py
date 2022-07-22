# ============================================
# Menentukan Posisi Dua Lingkaran
# --------------------------------------------

print(
    "========================================================================= \n",
    "Menentukan Posisi Dua Lingkaran \n",
    "-------------------------------------------------------------------------"
)

# 1. Pengguna menginput lingkaran 1.
x1, y1 = eval(input("Input titik pusat lingkaran 1 (contoh. 2,4) : "))
r1 = eval(input("Input jari-jari lingkaran 1 :"))
print("----------------------------------------------------------------------")

# 2. Program memvalidasi input ligkaran 1
if r1 > 0:
    if (x1 > 0 and y1 > 0):
        print(" \t Persamaan lingkaran 1 :",
            "(x -", abs(x1), ")^2 + ", "(y -", abs(y1), ")^2 = ", r1, "^2"
            )
    elif (x1 < 0 and y1 > 0):
        print("\t Persamaan lingkaran 1 :",
            "(x +", abs(x1), ")^2 + ", "(y -", abs(y1), ")^2 = ", r1, "^2"
            )
    elif (x1 > 0 and y1 < 0):
        print("\t Persamaan lingkaran 1 :",
            "(x -", abs(x1), ")^2 + ", "(y +", abs(y1), ")^2 = ", r1, "^2"
            )
    elif (x1 < 0 and y1 < 0):
        print("\t Persamaan lingkaran 1 :",
            "(x +", abs(x1), ")^2 + ", "(y +", abs(y1), ")^2 = ", r1, "^2"
            )
    elif (x1 == 0 and y1 > 0):
        print(
            "\t Persamaan Lingkaran 1 :",
            "x^2 +", "(y -", abs(y1), ") = ", r1, "^2"
            )
    elif (x1 == 0 and y1 < 0):
        print(
            "\t Persamaan Lingkaran 1 :",
            "x^2 + ", "(y +", abs(y1), ") = ", r1, "^2"
            )
    elif (x1 > 0 and y1 == 0):
        print(
            "\t Persamaan Lingkaran 1 :",
            "(x -", abs(x1), ")^2 +", "y^2 = ", r1, "^2"
            )
    elif (x1 < 0 and y1 == 0):
        print(
            "\t Persamaan Lingkaran 1 :",
            "(x +", abs(x1), ")^2 +", "y^2 = ", r1, "^2"
            )
    elif (x1 == 0 and y1 == 0):
        print(
            "\t Persamaan Lingkaran 1: ",
            "x^2 + y^2 = ", r1, "^2"
        )
    else:
        print("\t Input titik pusat lingkaran dengan pasangan bilangan..!")
else:
    print("\t Jari-jari lingkaran harus bilangan positif.")

print("-----------------------------------------------------------------------")

# 3. Pengguna menginput lingkaran 2.
x2, y2 = eval(input("Input titik pusat lingkaran 2 (contoh. 2,4) : "))
r2 = eval(input("Input jari-jari lingkaran 2 :"))

print("----------------------------------------------------------------------")

# 4. Program memvalidasi input ligkaran 2
if r2 > 0:
    if (x2 > 0 and y2 > 0):
        print("\t Persamaan lingkaran 2 :",
            "(x -", abs(x2), ")^2 + ", "(y -", abs(y2), ")^2 = ", r2, "^2"
            )
    elif (x2 < 0 and y2 > 0):
        print("\t Persamaan lingkaran 2 :",
            "(x +", abs(x2), ")^2 + ", "(y -", abs(y2), ")^2 = ", r2, "^2"
            )
    elif (x2 > 0 and y2 < 0):
        print("\t Persamaan lingkaran 2 :",
            "(x -", abs(x2), ")^2 + ", "(y +", abs(y2), ")^2 = ", r2, "^2"
            )
    elif (x2 < 0 and y2 < 0):
        print("\t Persamaan lingkaran 2 :",
            "(x +", abs(x2), ")^2 + ", "(y +", abs(y2), ")^2 = ", r2, "^2"
            )
    elif (x2 == 0 and y2 > 0):
        print(
            "\t Persamaan Lingkaran 2 :",
            "x^2 +", "(y -", abs(y2), ") = ", r2, "^2"
            )
    elif (x2 == 0 and y2 < 0):
        print(
            "\t Persamaan Lingkaran 2 :",
            "x^2 +", "(y +", abs(y2), ") = ", r2, "^2"
            )
    elif (x2 > 0 and y2 == 0):
        print(
            "\t Persamaan Lingkaran 2 :",
            "(x -", abs(x2), ")^2 +", "y^2 = ", r1, "^2"
            )
    elif (x2 < 0 and y2 == 0):
        print(
            "\t Persamaan Lingkaran 2 :",
            "(x +", abs(x2), ")^2 +", "y^2 = ", r2, "^2"
            )
    elif (x2 == 0 and y2 == 0):
        print(
            "\t Persamaan Lingkaran 2 : ",
            "x^2 + y^2 = ", r2, "^2"
        )
    else:
        print("\t Input titik pusat lingkaran dengan pasangan bilangan..!")
else:
    print("\t Jari-jari lingkaran harus bilangan positif.")

print("------------------------------------------------------------------------")

# 5. Hitung jarak titik pusat, jumlah jari2 dan selisih jari2
jarakTitikPusat = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

jumlahJari = r1 + r2

selisihJari = abs(r1 - r2)

print("------------------------------------------------------------------------")
# 6. Cek hubungan lingkaran 1 dengan lingkaran 2
if (x1 != x2 and y1 != y2):
    print("\t Titik pusat lingkaran 1 dan 2 tidak berimpit.")
    if selisihJari < jarakTitikPusat < jumlahJari:
        print("\t Lingkaran 1 dan 2 berpotongan di 2 titik.")
    elif jarakTitikPusat == jumlahJari:
        print("\t Lingkaran 1 dan 2 bersinggungan di luar.")
    elif jarakTitikPusat == selisihJari:
        print("\t Lingkaran 1 dan 2 bersinggungan di dalam.")
    else:
        print("\t Lingkaran 1 tidak berpotongan dengan lingkaran 2.") 
else:
    print("\t Lingkaran 1 sepusat dengan lingkaran 2 di titik", "(", x1, ",", y1, ")")


print("========================================================================")