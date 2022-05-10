# ================================================
# Menghitung besar sudut segitiga
# ================================================

# Mengimpor modul math
import math
print("===============================================")
print("Menghitung besar sudut segitiga")
print("-----------------------------------------------")

# Meminta pengguna menginput 3 titik
x1, y1 = eval(input("Input titik pertama (x1 , y1) : "))
x2, y2 = eval(input("Input titik pertama (x2 , y2) : "))
x3, y3 = eval(input("Input titik pertama (x3 , y3) : "))
print("-----------------------------------------------")

# Menentukan panjang sisi-sisi segitiga
a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Menentukan besar sudut segitiga
A = math.degrees( math.acos(( a ** 2 - b ** 2 - c ** 2 ) / ( -2 * b * c ) ) )
B = math.degrees( math.acos(( b ** 2 - a ** 2 - c ** 2 ) / ( -2 * a * c ) ) )
C = math.degrees( math.acos(( c ** 2 - a ** 2 - b ** 2 ) / ( -2 * a * b ) ) )

# Tampilkan hasil
print("Besar sudut A adalah : ", round(A, 2), "derajat")
print("Besar sudut B adalah : ", round(B, 2), "derajat")
print("Besar sudut C adalah : ", round(C, 2), "derajat")       

print("===============================================")
# ================================================