# =================================================
# Mengkonversi Desimal Ke Hexadesimal
# ---------------------------------------------------

print("================================================================ \n",
    "Mengkonversi Desimal Ke Hexadesimal \n",
    "-----------------------------------------------------------------"
    )
# Pengguna menginput bilangan antara 1 hingga 15
desimal = eval(input("Input Bilangan tidak kurang dari 1 dan tidak lebih dari 15 : "))

print("-----------------------------------------------------------------")

# Mengkonversi desimal ke hexadesimal

if 0 < desimal < 10:
    HEKSADESIMAL = desimal
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
elif desimal == 10:
    HEKSADESIMAL = "A"
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
elif desimal == 11:
    HEKSADESIMAL = "B"
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
elif desimal == 12:
    HEKSADESIMAL = "C"
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
elif desimal == 13:
    HEKSADESIMAL = "D"
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
elif desimal == 14:
    HEKSADESIMAL = "E"
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
elif desimal == 15:
    HEKSADESIMAL = "F"
    print("Bilangan desimal", desimal, "dapat diubah menjadi bilangan heksadesimal", HEKSADESIMAL)
else:
    HEKSADESIMAL = "Input salah...!!"
    print(HEKSADESIMAL, "Input bilangan tidak kurang dari 1 dan tidak lebih dari 15...!!!")

print("================================================================")