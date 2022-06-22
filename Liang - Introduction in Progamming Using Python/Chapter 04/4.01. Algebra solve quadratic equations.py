# ===================================================
# Menghitung Akar dari Persamaan Kuadrat
# ==================================================

print("=========================================\n",
        "Bentuk umum persamaan kuadrat adalah :\n",
        "a * x ** 2 + b * x + c = 0 \n",
        "Input a, b, dan c pada kolom di bawah ini\n",
        "Misal a = 1\n",
        "b = 4\n",
        "c = 9\n",
        "maka anda bisa menginputkan 1,4,9.\n",
        "------------------------------------"
      )

a, b, c = eval(input("Input a, b, c : "))

diskriminan = b ** 2 - 4 * a * c # hitung diskriminan
print("-----------------------------------------------")

# Mengecek nilai diskriminan
if diskriminan < 0 :
    print("Persamaan kuadrat tidak mempunyai akar real.") # diskriminan bernilai kurang dari 0
    print("===========================================")
elif diskriminan == 0:
    akar = - b / 2 * a
    print("Persamaan kuadrat mempunyai 1 akar real, yaitu :", akar) # diskriminan bernilai 0
    print("===========================================")
else:
    akar1 = (-b + diskriminan ** 0.5) / (2 * a) # diskriminan bernilai lebih dari 0
    akar2 = (-b - diskriminan ** 0.5) / (2 * a)
    print("Persamaan kuadrat mempunyai 2 akar real, yaitu :", akar1, "dan", akar2)
    print("===========================================")
