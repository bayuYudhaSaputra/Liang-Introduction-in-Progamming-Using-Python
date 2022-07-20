# ============================================
# Menentukan Posisi Garis Terhadap Segitiga
# ============================================

print("============================================================ \n",
    "Menentukan Posisi Garis Terhadap Segitiga \n",
    "-------------------------------------------------------------- \n",
    "Terdapat segitiga dengan titik sudut : \n",
    "\t A(0,0); B(200,0); C(0,100)",
    "sehingga persamaan garis sisi-sisi segitiga ABC adalah: \n",
    "\t AB: sumbu-x \n",
    "\t BC: x + 2y - 200 = 0 \n",
    "\t AC: sumbu-y \n",
    "Input titik sembarang dan program akan menentukan \n",
    "Apakah titik ada di dalam, berimpit atau di luar segitiga ABC \n",
    "--------------------------------------------------------------"
    )
# 1. Pengguna input titik sembarang
xp, yp = eval(input("Input titik sembarang (Mis. 5,6) :"))
print("--------------------------------------------------------------")

if (xp > 0 and yp > 0 and xp + 2 * yp - 200 < 0):
    print("Titik (", xp, ",", yp, ") di dalam segitiga ABC ")
elif (xp < 0 or yp < 0 or xp + 2 * yp - 200 > 0):
    print("Titik (", xp, ",", yp, ") di luar segitiga ABC ")
else:
    print("Titik (", xp, ",", yp, ") di keliling segitiga ABC ")

print("============================================================ \n")