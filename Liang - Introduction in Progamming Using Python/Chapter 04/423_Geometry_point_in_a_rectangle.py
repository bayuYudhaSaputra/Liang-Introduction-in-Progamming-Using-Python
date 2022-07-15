# =============================================================================
# Menentukan Hubungan Titik Terhadap Persegi Panjang Dalam Diagram Cartesius
# =============================================================================

print("============================================================================= \n",
    "Menentukan Hubungan Titik Terhadap Persegi Panjang Dalam Diagram Cartesius \n",
    "------------------------------------------------------------------------------- \n",
    "Diketahui : \n",
    "\t Persegi panjang ABCD dalam diagram cartesius dengan titik pusat O. \n",
    "\t dengan A(5 , 5/2); B(5 , -5/2); C(-5 , -5/2) dan D(-5 , 5/2). \n",
    "\t Input titik sembarang dan program akan menentukan titik tersebut berada \n",
    "\t a. di dalam persegi panjang atau, \n",
    "\t b. pada persegi panjang atau, \n",
    "\t c. di luar persegi panjang. \n",
    "-------------------------------------------------------------------------------"
    )

# Pengguna menginput titik sembarang
absisTitik, ordinatTitik = eval(input("Input titik sembarang :"))

# Menentukan jarak titik sembarang dengan titik O
jarak = (absisTitik ** 2 + ordinatTitik ** 2) ** (1/2)

# Menentukan setengah panjang diagonal
PANJANG_SETENGAH_DIAGONAL = (5 ** 2 + (5/2) ** 2) ** (1/2)

print("-------------------------------------------------------------------------------")
# Menguji hubungan titik dengan persegi panjang
if jarak < PANJANG_SETENGAH_DIAGONAL:
    print("Titik yang diinput berada di dalam persegi panjang.")
elif jarak == PANJANG_SETENGAH_DIAGONAL:
    print("Titik yang diinput berada di keliling persegi panjang.")
elif jarak > PANJANG_SETENGAH_DIAGONAL:
    print("Titik yang diinput berada di luar persegi panjang.")
else:
    print("Titik yang diinput tidak valid.")

print("=============================================================================")