# ============================================================================================
# Hitung zona waktu terhadap GMT
# --------------------------------------------------------------------------------------------

# Langkah 1. Ambil waktu saat ini
import time
waktuSaatIni = time.time()

# Langkah 2. Input zona waktu
gmtPlusN = eval(input("Input zona waktu (mis. -5 artinya zona waktu GMT-5) :"))

# Langkah 3. Hitung tambahan waktu terhadap GMT
waktuSaatIniPlusN = waktuSaatIni + 3600 * gmtPlusN

# Langkah 4. Selisih waktu (dalam detik) saat ini
#           dengan tengah malam tanggal 1 Januari 1970
totalDetik = int(waktuSaatIni)
totalDetikPlusN = int(waktuSaatIniPlusN)

# Langkah 5. Dapatkan detik saat ini
detikSaatIni = totalDetik % 60
detikSaatIniPlusN = totalDetikPlusN % 60

# Langkah 6. Dapatkan menit saat ini
totalMenit = totalDetik // 60
totalMenitPlusN = totalDetikPlusN // 60

# Langkah 7. Hitung menit saat ini dalam jam
menitSaatIni = totalMenit % 60
menitSaatIniPlusN = totalMenitPlusN % 60

# Langkah 8. Dapatkan total jam
totalJam = totalMenit // 60
totalJamPlusN = totalMenitPlusN // 60

# Langkah 9. Hitung jam saat ini
jamSaatIni = totalJam % 24
jamSaatIniPlusN = totalJamPlusN % 24

# Langkah 10. Tampilkan jam saat ini
print("=================================================================")
print("Saat ini pukul.")
print(jamSaatIni, ":", menitSaatIni, ":", detikSaatIni, "GMT")
print(jamSaatIniPlusN, ":",  menitSaatIni, ":", detikSaatIni, "GMT + ", "(", gmtPlusN, ")")
print("=================================================================")

# ============================================================================================