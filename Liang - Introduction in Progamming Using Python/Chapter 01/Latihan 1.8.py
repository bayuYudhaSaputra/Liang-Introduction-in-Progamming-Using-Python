# ================================================================
# Aproksimasi Luas dan Keliling Lingkaran Dengan Phi Berbeda
# ================================================================

phi1 = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
phi2 = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15)
r = 5.5
Luas1 = phi1 * r * r
Keliling1 = 2 * phi1 * r
Luas2 = phi2 * r * r
Keliling2 = 2 * phi2 * r

print("==========================================================")
print("Luas lingkaran dengan, ")
print("r = 5.5 ;")
print("phi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)")
print("adalah :")
print(Luas1)
print("----------------------------------------------------------")
print("Keliling lingkaran dengan, ")
print("r = 5.5 ;")
print("phi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)")
print("adalah :")
print(Keliling1)
print("----------------------------------------------------------")
print("Luas lingkaran dengan, ")
print("r = 5.5 ;")
print("phi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15)")
print("adalah :")
print(Luas2)
print("----------------------------------------------------------")
print("Keliling lingkaran dengan, ")
print("r = 5.5 ;")
print("phi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15)")
print("adalah :")
print(Keliling2)
print("==========================================================")