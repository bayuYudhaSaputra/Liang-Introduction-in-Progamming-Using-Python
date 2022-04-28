# ======================================================
# Hitung indeks wind-chill
# ------------------------------------------------------

# Langkah 1. Input temperatur udara antara - 58 hingga 41 (dalam satuan derajat Fahrenheit)
#               dan kecepatan angin dengan satuan mil per jam
ta = eval(input("Berapa fahrenheit suhu udara luar (suhu udara antara - 58 hingga 41 derajat fahrenheit) ?  "))
v = eval(input("Berapa mil per jam kecepatan angin di luar ruangan ?  "))
# ta adalah suhu udara luar dalam satuan derajat fahrenheit.
# v adalah kecepatan angin dengan satuan mil per jam

# Langkah 2. Hitung indeks wind-chill dengan rumus,
twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.6
# twc adalah indeks wind-chill

# Langkah 3. Tampilkan hasil perhitungan indeks wind-chill.
print("=========================================")
print("Indeks wind-chill dengan,")
print("-----------------------------------------")
print("Suhu udara luar", ta, "derajat fahrenheit")
print("kecepatan udara", v, "mil per jam")
print("-----------------------------------------")
print("adalah  ", round(twc,2))

# ======================================================