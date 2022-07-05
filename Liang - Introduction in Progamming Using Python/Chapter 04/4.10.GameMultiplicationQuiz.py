# ===============================
# Membuat Hasil Perkalian Acak
# ================================

print("===============================================")
import random
# membuat bilangan random antara 0 hingga 100
bil1 = random.randint(0,99)
bil2 = random.randint(0,99)

jawabanUser = eval(input("Berapakah hasil " + \
            str(bil1) + " * " + str(bil2) + " ? "
    ))

# Cek jawaban user dengan hasil perkalian
if jawabanUser == bil1 * bil2:
    print("Jawaban anda benar...!!")
else:
    print("Jawaban anda salah, " + str(bil1) + " * " + str(bil2) + "=" + str(bil1 * bil2) )

print("===============================================")