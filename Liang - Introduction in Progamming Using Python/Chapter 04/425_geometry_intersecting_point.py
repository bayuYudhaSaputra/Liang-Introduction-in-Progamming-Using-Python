# =======================================================
# Menentukan Perpotongan Dua Garis Dalam Bidang Cartesis
# =======================================================

print("=================================================================== \n",
    "Menentukan Perpotongan Dua Garis Dalam Bidang Cartesis \n",
    "--------------------------------------------------------------------"
    )
# Input dua titik yang melalui persamaan garis 1
x1, y1 = eval(input("Input titik ke-1 yang melalui persamaan garis 1 (Contoh. -1,2): "))
x2, y2 = eval(input("Input titik ke-2 yang melalui persamaan garis 1 (Contoh. 3,4): "))

print("--------------------------------------------------------------------")
# Menentukan koefisien x (a1), koefisien y (b1) dan konstanta (c1)
a1 = y2 - y1
b1 = -(x2 - x1)
c1 = x1 * (y2 - y1) - (x2 - x1) * y1
if b1 >= 0:
    print("Persamaan garis 1 adalah :",
        a1, "x", "+", b1, "y", "=", c1
        )
else:
    print("Persamaan garis 1 adalah :",
        a1, "x", "-", abs(b1), "y", "=", c1
        )
print("--------------------------------------------------------------------")

# Input dua titik yang melalui persamaan garis 2
x3, y3 = eval(input("Input titik ke-1 yang melalui persamaan garis 2 ( Contoh. 5,6 ): "))
x4, y4 = eval(input("Input titik ke-2 yang melalui persamaan garis 2 (Contoh. 1,1): "))
print("--------------------------------------------------------------------")

# Menentukan koefisien x (a2), koefisien y (b2) dan konstanta (c2)
a2 = y4 - y2
b2 = -(x4 - x3)
c2 = x3 * (y4 - y3) - (x4 - x3) * y3
if b2 >= 0:
    print("Persamaan garis 1 adalah :",
        a2, "x", "+", b2, "y", "=", c2
        )
else:
    print("Persamaan garis 1 adalah :",
        a2, "x", "-", abs(b2), "y", "=", c2
        )

print("--------------------------------------------------------------------")
# Menentukan titik potong (xp,yp)
pembilangAbsis = c1 * b2 - b1 * c2
penyebutAbsis = a1 * b2 - a2 * b1
pembilangOrdinat = c1 * a2 - a1 * c2
penyebutOrdinat = b1 * b2 - a1 * b2

if (pembilangAbsis == 0 or penyebutAbsis == 0 or pembilangAbsis == 0 or penyebutOrdinat == 0):
    print("Garis 1 dan 2 berimpit")
elif (penyebutAbsis == 0 or penyebutOrdinat == 0):
    print("Garis 1 dan 2 sejajar")
else:
    xp = pembilangAbsis / penyebutAbsis
    yp = pembilangOrdinat / penyebutOrdinat
    print("Garis 1 dan 2 berpotongan di titik",
        "(", xp, ",", yp, ")"
        )

print("====================================================================")