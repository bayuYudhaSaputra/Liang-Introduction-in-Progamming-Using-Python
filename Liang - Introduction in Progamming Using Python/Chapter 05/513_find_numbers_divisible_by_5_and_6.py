count = 0
print("\n============================================================")
print("Bilangan habis dibagi 5 atau 6 tapi bukan keduanya.")
print("------------------------------------------------------------\n")
for bilangan in range(100,200):
    if (bilangan % 5 == 0 or bilangan % 6 == 0) and \
        (not(bilangan % 5 == 0 and bilangan % 6 == 0)):
        # bilangan habis dibagi 5 atau 6 tetapi tidak keduanya
        print(bilangan, end = ' ')
        count += 1
        if count % 10 == 0:
            # Setiap baris hanya berisi 10 bilangan
            print("\n")
print("\n")
print("------------------------------------------------------------\n")