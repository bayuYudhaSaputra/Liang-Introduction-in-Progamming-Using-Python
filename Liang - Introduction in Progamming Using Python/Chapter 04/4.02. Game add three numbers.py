# =========================================
# Game Tebak Jumlah 3 Bilangan
# =========================================

import random

# Mengacak 3 bilangan cacah 1 digit.
bilangan1 = random.randint(0,9)
bilangan2 = random.randint(0,9)
bilangan3 = random.randint(0,9)

# jumlah 3 bilangan acak
jumlah = bilangan1 + bilangan2 + bilangan3

# Pengguna menginput 3 jawaban
jawaban = eval(input("Berapa hasil dari " + str(bilangan1) + " + " + str(bilangan2) + " + " + str(bilangan3) + " ? "))

# Membandingkan jawaban dengan jumlah
print(
    "jawaban",
    bilangan1, " + ", bilangan2, " + ", bilangan3,
    "adalah",
    jumlah == jawaban
)