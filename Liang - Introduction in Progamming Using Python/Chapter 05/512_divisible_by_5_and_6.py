print("----------------------------------------------------------\n",
    "Bilangan antara 100 hingga 1000 yang habis dibagi 5 dan 6\n",
    "------------------------------------------------------------"
    )
count = 0
for bilangan in range(100, 1000 + 1):
    if bilangan % 5 == 0 and bilangan % 6 == 0:
        # bilangan habis dibagi 5 dan 6
        print(format(bilangan, "5d"), end = ' ')
        count += 1
        if count % 10 == 0:
            # Setiap baris hanya berisi 10 bilangan
            print("\n")

print("----------------------------------------------------------")