# =============================================
# Point Position
# =============================================
import sys

print("========================================================= \n",
    "Posisi titik terhadap garis \n",
    "------------------------------------------------------------"
    )
x1, y1 = eval(input("Input titik pertama suatu persamaan garis :  "))
x2, y2 = eval(input("Input titik kedua suatu persamaan garis :  "))
xp, yp = eval(input("Input titik sembarang : "))

print("------------------------------------------------------------")
# Menampilkan persamaan garis
if (x2 - x1 == 0 and y2 - y1 == 0):
    print("\t Kedua titik tidak membentuk persamaan garis")
    print("=========================================================")
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

# Menentukan hubungan garis dengan titik sembarang (indeks p)
if (y2 - y1 == 0):
    p = y1
    if (p > yp):
        print("\t Titik (",xp, ",",yp,") di bawah","persamaan garis y =", y1)
    elif (p < yp):
        print("\t Titik (",xp, ",",yp,") di atas","persamaan garis y =", y1)
    else:
        print("\t Titik (",xp, ",",yp,") berimpit dengan","persamaan garis y =", y1)
else:    
    p = (x2 - x1) * (yp - y1) + (xp - x1) * (y2 - y1)
    if (p > 0):
        print("\t Titik (", xp, ",", yp, ") di sisi kiri garis")
    elif (p < 0):
        print("\t Titik (", xp, ",", yp, ") di sisi kanan garis")
    else:
        print("\t Titik (", xp, ",", yp, ") berimpit dengan garis")

print("=========================================================")
