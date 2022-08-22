print("----------------------------------------------------------\n",
    "Bilangan antara 100 hingga 1000 yang habis dibagi 5 dan 6\n",
    "----------------------------------------------------------"
    )
for i in range(0,30,10):
    for j in range(4,14):
        bilangan = (i + j) * 30
        print(format(bilangan,"5d"), end = '')
    print("\n")

print("----------------------------------------------------------")