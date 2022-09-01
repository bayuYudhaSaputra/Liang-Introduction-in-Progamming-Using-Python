# =========================================================================
# Count Positive and Negative Numbers and Compute the Average of Numbers
# -------------------------------------------------------------------------

print("================================================================== \n",
    "Menghitung jumlah dan rata-rata bilangan positif dan negatif \n",
    "--------------------------------------------------------------------"
    )
inputBilangan = eval(input("Input bilangan integer" + 
                "(program akan berhenti jika anda menginput 0) : "))

sum = 0
banyakPerulangan = 0
banyakNegatif = 0

if inputBilangan == 0:
    print("Anda tidak menginput bilangan sama sekali.")
else:
    while inputBilangan != 0:
        sum += inputBilangan
        banyakPerulangan += 1 # menghitung banyak perulangan
        rata2 = sum / banyakPerulangan
    
        if inputBilangan < 0:
            banyakNegatif += 1 # menghitung banyak bilangan negatif yang diinput
    
        inputBilangan = eval(input("Input bilangan integer" + 
                "(program akan berhenti jika anda menginput 0) : "))

    print("Jumlah bilangan yang diinput adalah", sum)
    print("Rata-rata bilangan yang diinput adalah", rata2)
    print("Banyak bilangan negatif yang diinput adalah", banyakNegatif)
