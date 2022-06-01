# ===========================================================
# Penghitungan Gaji
# ===========================================================

print("==============================================")
print("Penghitungan Gaji")
print("----------------------------------------------")
# 1. Input data-data sebagai berikut:
namaKaryawan = input("Input nama karyawan : ")
jamKerja = eval(input("Input Lama kerja dalam seminggu dengan satuan jam : "))
gajiPerJam = eval(input("Input gaji per jam : USD."))
persenPajakFederal = eval(
    input("Input persentase pajak Federal (Mis. 10 artinya 10%) : "))
persenPajakNegaraBagian = eval(
    input("Input persentase pajak negara bagian (Mis. 5 artinya 5%) : "))
print("--------------------------------------------")

# 2. Hitung gaji kotor yang diterima
gajiKotor = jamKerja * gajiPerJam

# 3. Hitung pengurang gaji
pajakFederal = (persenPajakFederal / 100) * gajiKotor
pajakNegaraBagian = (persenPajakNegaraBagian / 100) * gajiKotor
totalPengurangGaji = pajakFederal + pajakNegaraBagian

# 4. Hitung nominal gaji bersih
gajiBersih = gajiKotor - totalPengurangGaji

# 5. Tampilkan hasil
print(
    "Nama Karyawan : ",
    namaKaryawan,
    "."
)

print(
    "Lama kerja dalam satu minggu :",
    int(jamKerja),
    "jam."
)

print(
    "Nominal Gaji per jam : ",
    "USD.", round(gajiPerJam,2)
)

print(
    "Gaji kotor :",
    "USD.", round(gajiKotor,2)
)

print("-------------------------------------")
print("Pengurang Gaji :")

print("\t Pajak Federal ",
    "(", persenPajakFederal, "%) :",
    "USD.", round(pajakFederal,2)
)

print("\t Pajak negara bagian ",
    "(", persenPajakNegaraBagian, "%) :",
    "USD.", round(pajakNegaraBagian,2)
)

print("\t Total pengurang gaji :",
    "USD.", round(totalPengurangGaji,2)
)

print("---------------------------------------")

print(
    "Total gaji bersih :",
    "USD.", round(gajiBersih,2)
)

print("========================================")
