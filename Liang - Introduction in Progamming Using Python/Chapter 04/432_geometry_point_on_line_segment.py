# ================================================
# Menentukan Posisi Titik dengan Garis
# ================================================
print("========================================================= \n",
    "Posisi titik terhadap garis \n",
    "------------------------------------------------------------"
    )

import sys

# Pengguna menginput 2 titik pembentuk garis
x1, y1 = eval(input("Input titik ke-1 yang membentuk garis : "))
x2, y2 = eval(input("Input titik ke-2 yang membentuk garis : "))

print("------------------------------------------------------------")

# Menampilkan persamaan garis
if (x2 - x1 == 0 and y2 - y1 == 0):
    print("\t Kedua titik tidak membentuk persamaan garis")
    print("==========================================================")
    sys.exit()
elif (x2 - x1 == 0):
    print("\t Persamaan garis: x =", x1 )
elif (y2 - y1 == 0):
    print("\t Persamaan garis: y =", y1)
else:
    # menentukan gradien (m)
    m = (y2 - y1) / (x2 - x1)
    c = y1 - x1
    if (y1 - x1 > 0):
        print("\t Persamaan garis :",
            "y = ", m, "x +", c
            )
    elif (y1 - x1 < 0):
        print("\t Persamaan garis :",
            "y = ", m, "x -", abs(c)
            )
    else:
        print("\t Persamaan garis :",
            "y = ", m, "x"
            )        
print("------------------------------------------------------------")


# Pengguna menginput 1 titik sembarang
xp, yp = eval(input("Input titik sembarang: "))
print("------------------------------------------------------------")

# Program mengecek hubungan titik dengan garis
if (x2 - x1 == 0):
    if xp == x1:
        print("\t Titik (", xp, ",", yp, "berimpit dengan garis")
    else:
        print("\t Titik (", xp, ",", yp, "tidak berimpit dengan garis")
elif (y2 - y1 == 0):
    if yp == y1:
        print("\t Titik (", xp, ",", yp, "berimpit dengan garis y")
    else:
        print("\t Titik (", xp, ",", yp, "tidak berimpit dengan garis y")
else:
    p = (x2 - x1) * (yp - y1) + (xp - x1) * (y2 - y1)
    if (p == 0):
        print("\t Titik (", xp, ",", yp, ") berimpit dengan garis")
    else:
        print("\t Titik (", xp, ",", yp, ") tidak berimpit dengan garis")

print("==========================================================")