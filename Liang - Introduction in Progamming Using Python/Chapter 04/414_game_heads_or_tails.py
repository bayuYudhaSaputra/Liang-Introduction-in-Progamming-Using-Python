import random

# ====================================
# Lempar Koin
# ====================================

koinRandom = random.randrange(0,1)
print("================================================")
print("Input : \n",
        "\t 0 jika anda memilih sisi GAMBAR pada koin \n",
        "\t \t atau \n",
        "\t 1 jika anda memilih sisi ANGKA pada koin.")
print("-------------------------------------------------")
tebakanUser = eval(input("Input bilangan 1 atau 0 : "))
print("-------------------------------------------------")

if tebakanUser == 0:
    print("Anda memilih sisi GAMBAR")
elif tebakanUser == 1:
    print("Anda memilih sisi ANGKA")
else:
    print("")

if koinRandom == 0:
    print("Muncul sisi koin GAMBAR")
else:
    print("Muncul sisi koin ANGKA")

if koinRandom == tebakanUser:
    print("Jawaban anda tepat..!!")
else:
    print("Jawaban anda salah..!!")

print("================================================")