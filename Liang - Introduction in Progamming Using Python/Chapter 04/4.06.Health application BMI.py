# ==============================================
# Menentukan BMI
# ==============================================

# Pengguna menginput berat badan dalam satuan pound
berat = eval(input("Input berat badan dalam satuan pound : "))

# Pengguna menginput tinggi badan dalam satuan kaki
tinggiDalamFeet =  eval(input("Input tinggi badan dalam satuan kaki (Feet) : "))

# Pengguna menginput tinggi badan dalam satuan inchi.
tinggiDalamInchi = eval(input("Input tinggi badan dalam satuan inchi : "))

# Mendefinisikan 1 Kg ke Pound
KILOGRAM_PER_POUND = 0.45359237 # Konstanta

# Mendefinsikan 1 inchi ke meter
METER_PER_INCHI = 0.0254 # Konstanta

# Mendefiniskan 1 feet ke meter
METER_PER_FEET = 0.3048 # Konstanta

# Menghitung BMI
beratDalamKilogram = berat * KILOGRAM_PER_POUND
beratDalamMeter = tinggiDalamFeet * METER_PER_FEET + tinggiDalamInchi * METER_PER_INCHI
bmi = beratDalamKilogram / (beratDalamMeter ** 2)

# Menampilkan hasil BMI
print("BMI dengan berat", berat, "pound dan",
    "tinggi", tinggiDalamFeet, "feet",
    tinggiDalamInchi, "inchi adalah : ",
    format(bmi, ".2f")
    )

if bmi < 18.5:
    print("Anda termasuk Underweight")
elif bmi < 25:
    print("Anda termasuk Normal")
elif bmi < 30:
    print("Anda termasuk Overweight.")
else:
    print("Anda termasuk Obese.")