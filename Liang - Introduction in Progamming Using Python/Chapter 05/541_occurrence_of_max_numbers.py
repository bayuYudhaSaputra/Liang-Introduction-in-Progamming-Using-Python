bilangan = eval(input("Input suatu bilangan (Input 0 jika ingin mengakhiri program) :"))
bilanganTerbesar = bilangan
banyakBilanganTerbesar = 0

while bilangan != 0:
    bilangan = eval(input("Input suatu bilangan (Input 0 jika ingin mengakhiri program) :"))
    if bilangan >= bilanganTerbesar:
        bilanganTerbesar = bilangan
        
        banyakBilanganTerbesar += 1

print("Bilangan terbesar = ", bilanganTerbesar)
print("Banyak bilangan terbesar = ", banyakBilanganTerbesar)