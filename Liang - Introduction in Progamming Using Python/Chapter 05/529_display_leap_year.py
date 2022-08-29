print("\n------------------------------------------------")
print("Daftar Tahun Kabisat Mulai 2001 hingga 2100")
print("------------------------------------------------\n")
count = 0
for tahun in range(2001, 2101):

    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print(tahun, end = ' ')
        count += 1
        if count % 10 == 0:
            print("\n")
print("\n------------------------------------------------\n")