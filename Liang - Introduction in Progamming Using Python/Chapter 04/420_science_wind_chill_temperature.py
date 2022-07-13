# ======================================================
# Hitung indeks wind-chill
# ------------------------------------------------------

# Langkah 1. Input temperatur udara antara - 58 hingga 41 (dalam satuan derajat Fahrenheit)
#               dan kecepatan angin dengan satuan mil per jam

print("==================================================================================== \n",
    "Indeks Widchill \n",
    "---------------------------------------------------------------------------------------"
    )

# Langkah 1. Input temperatur udara antara - 58 hingga 41 (dalam satuan derajat Fahrenheit)
#               dan kecepatan angin dengan satuan mil per jam
ta = eval(input("Berapa fahrenheit suhu udara luar (suhu udara antara - 58 hingga 41 derajat fahrenheit) ?  "))
v = eval(input("Berapa mil per jam kecepatan angin di luar ruangan ?  "))
# ta adalah suhu udara luar dalam satuan derajat fahrenheit.
# v adalah kecepatan angin dengan satuan mil per jam

print("----------------------------------------------------------------------------------")

if -53 < ta < 41:
    if v >= 2:
        twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.6
        print("Indeks wind-chill dengan,")
        print("\t Suhu udara luar", ta, "derajat fahrenheit")
        print("\t kecepatan udara", v, "mil per jam")
        print("\t adalah  ", round(twc,2))
        print("====================================================================================")
else:
    print("Input tidak valid, \n",
    "suhu luar yang valid antara -53 hingga 41 derajat Fahrenheit..!\n ",
    "Dan kecepatan angin tidak kurang dari 2 mil/jam..!! \n",
    "=============================================================================================="
    )