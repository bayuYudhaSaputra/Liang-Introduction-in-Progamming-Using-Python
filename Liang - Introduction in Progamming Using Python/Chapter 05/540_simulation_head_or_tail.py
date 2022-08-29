import random

print("\n------------------------------------------------------------")
print("|", format("Lemparan Ke-","12s"), "|", format("Koin Yang Muncul","15s"), "|")
print("------------------------------------------------------------\n")
for i in range(1, 1000 + 1):
    bilanganRandom = random.randint(0,1)
    if bilanganRandom == 0:
        koinRandom = "Angka"
    else:
        koinRandom = "Gambar"
    print("|", format(i,"12d"), "|", format(koinRandom, "15s"), "|")
print("------------------------------------------------------------\n")