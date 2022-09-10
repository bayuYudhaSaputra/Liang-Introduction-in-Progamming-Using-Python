banyakSuku = 4
faktorial = 1

for n in range(banyakSuku + 1, 0, -1):

    for n in range(banyakSuku, 0, -1):
        faktorial *= n
        print(faktorial)

    suku = 1 / faktorial
    print(suku)