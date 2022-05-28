# ===============================================
# Hitung jarak dua titik Latitude dan Longitude
# ===============================================

print("==========================================")
print("Jarak Dua Titik Latitude dan Longitude")
print("------------------------------------------")

import math
radiusBumi = 6371.01

# 1. Input titik ke-1 (Latitude dan Longitude)
titikX1, titikY1 = eval(input("Input titik ke-1 (Latitude dan Longitude) (Mis. (3.12, -4.01)) dalam derajat : "))
x1, y1 = math.radians(titikX1), math.radians(titikY1)

# 2. Input titik ke-2 (Latitude dan Longitude)
titikX2, titikY2 = eval(input("Input titik ke-2 (Latitude dan Longitude) (Mis. (-5.12, 4.01)) dalam derajat: "))
x2, y2 = math.radians(titikX2), math.radians(titikY2)

# 3. Hitung jarak kedua titik
jarak = radiusBumi * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y2 - y1))

# 4. Tampilkan hasil perhitungan
print("Jarak antara titik \n",
        "(", titikX1, ",", titikY1, ")\n",
        "dengan",
        "(", titikX2, ",", titikY2, ")\n",
        "adalah",
        jarak, "Km."
        )

print("==========================================")