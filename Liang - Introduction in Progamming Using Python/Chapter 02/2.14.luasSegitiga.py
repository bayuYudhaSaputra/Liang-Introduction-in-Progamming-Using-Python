# ==========================================================================================================
# Menghitung Luas Segitiga
# ----------------------------------------------------------------------------------------------------------

# Langkah 1. Input titik sudut ke-1, ke-2 dan ke-3
x1 , y1 = eval(input("Input titik sudut ke-1 segitiga (misal. ( 0,0 )):"))
x2 , y2 = eval(input("Input titik sudut ke-2 segitiga (misal. ( 6,0 )):"))
x3 , y3 = eval(input("Input titik sudut ke-3 segitiga (misal. ( 3,5 )):"))

# Langkah 2. Hitung jarak titik sudut ke-1 dengan ke-2, dengan rumus :
panjangSisi1 = ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2) ** 0.5

# Langkah 3. Hitung jarak titik sudut ke-2 dengan ke-3
panjangSisi2 = ( ( x2 - x3 ) ** 2 + ( y2 - y3 ) ** 2 ) ** 0.5

# Langkah 4. Hitung jarak titik sudut ke-1 dengan ke-3 dengan rumus :
panjangSisi3 = ( (x1 - x3) ** 2 + ( y1 - y3 ) ** 2 ) ** 0.5

# Langkah 5. Hitung setengah dari keliling segitiga dengan rumus :
setengahKeliling = 0.5 * (panjangSisi1 + panjangSisi2 + panjangSisi3)

# Langkah 6. Hitung luas segitiga dengan rumus :
luasSegitiga = ( setengahKeliling * ( setengahKeliling - panjangSisi1 ) * ( setengahKeliling - panjangSisi2 ) * ( setengahKeliling - panjangSisi3 ) ) ** 0.5

# Langkah 7. Tampilkan luas segitiga
print(
        "Luas segitiga dengan titik sudut,",
        "(", x1, ",", y1, ")", ";",
        "(", x2, ",", y2, ")", ";",
        "(", x3, ",", y3, ")",
        "adalah :",
        luasSegitiga,
        "satuan luas"
    )

# ==========================================================================================================