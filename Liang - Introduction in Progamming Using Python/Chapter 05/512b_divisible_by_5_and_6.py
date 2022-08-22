print("----------------------------------------------------------\n",
    "Bilangan antara 100 hingga 1000 yang habis dibagi 5 dan 6\n",
    "----------------------------------------------------------"
    )
i = 0
while i < 30:
    j = 4
    while j <= 13:
        bilangan = (i + j) * 30
        print(format(bilangan, "5d"), end = '')
        j += 1
    print("\n")
    i += 10

print("----------------------------------------------------------")