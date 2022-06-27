# ================================================
# Find Future Dates
# ================================================

print("============================================ \n",
      "Menemukan hari \n",
      "--------------------------------------------- \n",
      "Input bilangan : \n",
      "\t 0 : untuk hari Minggu \n",
      "\t 1 : untuk hari Senin \n",
      "\t 2 : untuk hari Selasa \n",
      "\t 3 : untuk hari Rabu \n",
      "\t 4 : untuk hari Kamis \n",
      "\t 5 : untuk hari Jumat \n",
      "\t 6 : untuk hari Sabtu \n",
      "---------------------------------------------"
      )
indeksHariIni = eval(input("Input indeks untuk hari ini : "))

# Menentukan hari berdasarkan indeks
if indeksHariIni == 0:
    print("Hari ini adalah hari Minggu.")
elif indeksHariIni == 1:
    print("Hari ini adalah hari Senin.")
elif indeksHariIni == 2:
    print("Hari ini adalah hari Selasa.")
elif indeksHariIni == 3:
    print("Hari ini adalah hari Rabu.")
elif indeksHariIni == 4:
    print("Hari ini adalah hari Kamis.")
elif indeksHariIni == 5:
    print("Hari ini adalah hari Jumat")
elif indeksHariIni == 6:
    print("Hari ini adalah hari Sabtu.")
else:
    print("Input bilangan antara 0 hingga 6.")

banyakHariSetelahHariIni = eval(input("Input banyak hari setelah hari ini : "))

# Jumlah indeks hari ini dengan banyak hari setelahnya.
indeksHariBerikutnya = (indeksHariIni + banyakHariSetelahHariIni) % 7

# Menentukan hari selanjutnya berdasarkan indeks
if indeksHariBerikutnya == 0:
    print("Hari ini adalah hari Minggu.")
elif indeksHariBerikutnya == 1:
    print("Hari ini adalah hari Senin.")
elif indeksHariBerikutnya == 2:
    print("Hari ini adalah hari Selasa.")
elif indeksHariBerikutnya == 3:
    print("Hari ini adalah hari Rabu.")
elif indeksHariBerikutnya == 4:
    print("Hari ini adalah hari Kamis.")
elif indeksHariBerikutnya == 5:
    print("Hari ini adalah hari Jumat")
elif indeksHariBerikutnya == 6:
    print("Hari ini adalah hari Sabtu.")
else:
    print("Input bilangan antara 0 hingga 6.")

print("============================================")