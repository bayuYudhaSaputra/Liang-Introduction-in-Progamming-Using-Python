# =======================================
# Konversi RMB ke USD Dan Sebaliknya
# =======================================

import sys
print("================================================ \n",
    "Konversi RMB ke USD Dan Sebaliknya \n",
    "--------------------------------------------------"
    )

# Konversi 1 USD menjadi RMB
konversiRMBKeUSD = eval(input("Input nilai tukar USD (US Dollar)terhadap RMB (Renminbi) : "))
print("------------------------------------------------")

print("Keterangan :\n",
    "\t Input 0 jika mengkonversi USD ke RMB \n",
    "\t Input 1 jika mengkonversi RMB ke USD \n"
    )

# Input 0 atau 1 untuk mengkonversi USD ke RMB atau sebaliknya
indeksKonversi = eval(input("Input 0 atau 1 : "))
print("------------------------------------------------")

if indeksKonversi == 0:
    uangUSD = eval(input("Input mata uang dalam USD : USD. "))
    uangRMB = konversiRMBKeUSD * uangUSD
    print("USD.", uangUSD, " = RMB.", uangRMB)
    print("================================================")
    sys.exit()
elif indeksKonversi == 1:
    uangRMB = eval(input("Input mata uang dalam RMB : RMB. "))
    uangUSD = uangRMB / konversiRMBKeUSD
    print("RMB. ", uangRMB, " = USD. ", uangUSD)
    print("================================================")
    sys.exit()
else:
    print("Input anda salah ... Input 0 atau 1 saja..!")
    print("================================================")
    sys.exit()