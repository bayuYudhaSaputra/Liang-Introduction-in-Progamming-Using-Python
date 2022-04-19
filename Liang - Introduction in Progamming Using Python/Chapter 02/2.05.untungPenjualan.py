# ==================================================================================
# Hitung Harga Penjualan
# ----------------------------------------------------------------------------------
# Langkah 1. Input harga pembelian dan persentase untung
# Langkah 2. Hitung untung dengan rumus : untung = (persenUntung / 100) * hargaBeli
# Langkah 3. Hitung harga penjualan dengan rumus : hargaJual = hargaBeli + untung
# Langkah 4. Tampilkan harga penjualan
# ----------------------------------------------------------------------------------

# Langkah 1. Input harga pembelian dan persentase untung
hargaBeli, persenUntung = eval(input("Input Harga beli (misal. Rp100000) dan persentase untung (misal. 5%) :"))

# Langkah 2. Hitung untung
untung = (persenUntung / 100) * hargaBeli

# Langkah 3. Hitung harga penjualan
hargaJual = hargaBeli + untung

# Langkah 4. Tampilkan harga penjualan
print(
    "Jika barang dibeli dengan harga Rp", 
    hargaBeli,
    "dengan untung",
    persenUntung, 
    "%",
    "maka harga jualnya adalah : Rp",
    hargaJual
    )
# ==================================================================================