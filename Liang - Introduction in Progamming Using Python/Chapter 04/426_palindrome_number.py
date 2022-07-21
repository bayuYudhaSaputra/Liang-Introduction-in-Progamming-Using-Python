# ===========================================
# Menguji bilangan polindrom
# ===========================================
# Contoh bilangan polindrom = 121.
# -------------------------------------------

print("=========================================== \n",
    "Menguji bilangan polindrom \n",
    "-------------------------------------------"
    )
# Pengguna menginput bilangan 3 digit
bilangan = eval(input("Input bilangan integer 3 digit : " ))

# Ekstrak bilangan tersebut menjadi ratusan, puluhan dan satuan
ratusan = bilangan // 100
sisaRatusan = bilangan % 100

puluhan = sisaRatusan // 10
satuan = sisaRatusan % 10

# menentukan apakah bilangan yang diinput adalah bilangan polindrome
if 100 <= bilangan < 1000:
    if ratusan == satuan:
        print("Bilangan", bilangan, "adalah bilangan polindrom.")
    else:
        print("Bilangan", bilangan, "bukan bilangan polindrom.")
else:
    print("Anda tidak menginput bilangan integer 3 digit.")

print("===========================================")