print("\n------------------------------------------------")
print("Daftar Tahun Kabisat Mulai 2001 hingga 2100")
print("------------------------------------------------\n")


for tahun in range(2001, 2101):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print(tahun)
    