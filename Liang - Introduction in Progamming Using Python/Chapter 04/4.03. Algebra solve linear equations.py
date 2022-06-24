# ==================================================
# Menentukan Penyelesaian Sistem Persamaan Linier
# ==================================================

print("=============================================\n",
        "Sistem Persamaan Linier\n",
        "-------------------------------------------\n",
        "Sistem persamaan linier :\n",
        "a * x + b * y = e \n",
        "c * x + d * y = f \n",
        "mempunyai penyelesaian, \n",
        "x = (e * d - b * f) / a * d - b * c \n",
        "y = (a * f - e * c) / a * d - b * c \n",
        "----------------------------------------------- \n",
        "Untuk menentukan pernyelesaian sistem persamaan linier ini,\n",
    )

# Input a, b, c, d, e dan f
a, b, c, d, e, f = eval(input("Input a, b, c, d, e dan f : "))

# Hitung determinan
determinan = a * d - b * c

# Periksa nilai determinan
if determinan == 0 :
    print("Sistem persamaan linier : \n" + \
        "\t" + str(a) + "x + " + str(b) + "y = " + str(e) + "\n" + \
         "\t" + str(c) + "x + " + str(d) + "y = " + str(f) + "\n" + \
        "Tidak mempunyai penyelesaian."
    )
else :
    x = (e * d - b * f) / a * d - b * c
    y = (a * f - e * c) / a * d - b * c
    print("Penyelesaian sistem persamaan linier \n" + \
        "\t" + str(a) + "x + " + str(b) + "y = " + str(e) + "\n" + \
         "\t" + str(c) + "x + " + str(d) + "y = " + str(f) + "\n" + \
        "adalah : \n" + \
        "\t x = " + str(x) + ",\n" + \
        "\t y = " + str(y)
    )
print("================================================================")