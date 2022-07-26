# =================================================
# Mengkonversi Heksadesimal Ke Desimal
# --------------------------------------------------

print("================================================================ \n",
    "Mengkonversi Heksadesimal Ke Desimal \n",
    "-----------------------------------------------------------------"
    )
# Pengguna menginput heksadesimal
heksadesimal = input("Input heksadesimal antara 1 hingga F: ")

print("-----------------------------------------------------------------")

# Mengkonversi heksadesimal ke desimal

if (heksadesimal == "1" or \
    heksadesimal == "2" or \
    heksadesimal == "3" or \
    heksadesimal == "4" or \
    heksadesimal == "5" or \
    heksadesimal == "6" or \
    heksadesimal == "7" or \
    heksadesimal == "8" or \
    heksadesimal == "9"):
    DESIMAL = heksadesimal
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
elif heksadesimal == "A":
    DESIMAL = 10
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
elif heksadesimal == "B":
    DESIMAL = 11
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
elif heksadesimal == "C":
    DESIMAL = 12
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
elif heksadesimal == "D":
    DESIMAL = 13
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
elif heksadesimal == "E":
    DESIMAL = 14
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
elif heksadesimal == "F":
    DESIMAL = 15
    print("Bilangan heksadesimal", heksadesimal, "dapat diubah menjadi bilangan desimal", DESIMAL)
else:
    DESIMAL = "Input salah"
    print(DESIMAL)

print("================================================================")