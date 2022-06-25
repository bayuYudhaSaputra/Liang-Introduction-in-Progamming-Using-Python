# ============================================
# Games Bilangan Random
# ===========================================

import random

# membuat bilangan random
bilanganAcak1 = random.randint(10, 99)
bilanganAcak2 = random.randint(10, 99)

# jumlah bilangan random
hasil = bilanganAcak1 + bilanganAcak2

print(
    "===================================\n",
    "\t Games Bilangan Random \n",
    "-----------------------------------"
)

# User menginput hasil penjumlahan bilangan random
userInput = eval(input("Berapakah hasil dari" +
                       str(bilanganAcak1) + " + " + str(bilanganAcak2) + " ? "
                       ))
print("----------------------------------")
# Periksa jawaban dari user
if userInput == hasil:
    print("Jawaban anda benar!!!")
else:
    print("Jawaban anda salah!!")

print("===================================")