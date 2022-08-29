print("\n------------------------------------------------------")
print("Menentukan Mean dan Standar Deviasi")
print("------------------------------------------------------")

suku = 0
jumlahData = 0
jumlahKuadratData = 0


banyakData = eval(input("Berapa banyak data yang diinput? "))
print("\n------------------------------------------------------\n")

if banyakData <= 0:
    print("Anda harus menginput paling tidak 1 data")
    print("\n------------------------------------------------------\n")
else:
    for i in range(1, banyakData + 1):
        print("Input data ke-", i, " : (setelah tanda =>)")
        suku = eval(input("=> "))
        jumlahData += suku
        jumlahKuadratData += suku ** 2

    mean = jumlahData / banyakData
    varians = ((jumlahKuadratData) - ((jumlahData ** 2) / banyakData)) / (banyakData - 1)
    simpanganBaku = varians ** (1/2)
    print("\n------------------------------------------------------\n")
    print("Mean data-data tersebut adalah ", format(mean, ".3f"))
    print("Simpangan baku data-data tersebut adalah ", format(simpanganBaku, ".3f"))
    print("\n------------------------------------------------------\n")