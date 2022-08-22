BANYAK_BILANGAN_PER_BARIS = 10
bilangan = 100

while bilangan <= 1000:
    if bilangan % 5 == 0 and bilangan % 6 == 0:
        print(format(bilangan,"4d"), end = '')
    bilangan += 1