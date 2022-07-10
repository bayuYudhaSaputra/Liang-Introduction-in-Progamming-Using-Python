import sys
import random

# mengacak indeks
indeksKomputer = random.randint(0,2)

# mengubah indeks menjadi gunting, batu atau kertas
if indeksKomputer == 0:
    komputer = "Gunting"
elif indeksKomputer == 1:
    komputer = "Batu"
else:
    komputer = "Kertas"

print("===================================== \n",
    "Permainan Gunting, Batu, Kertas. \n",
    "-------------------------------------- \n",
    "Keterangan : \n",
    "\t Input 0 jika anda memilih Gunting. \n",
    "\t Input 1 jika anda memilih Batu. \n",
    "\t Input 2 jika anda memilih Kertas. \n",
    "--------------------------------------"
    )
# User menginput indeks
indeksPengguna = eval(input("Input pilihan anda : "))

# Mengubah indeks menjadi gunting, batu, kertas
if indeksPengguna == 0:
    pengguna = "Gunting"
elif indeksPengguna == 1:
    pengguna = "Batu"
elif indeksPengguna == 2:
    pengguna = "Kertas"
else:
    pengguna = "Indeks hanya boleh diinput bilangan 0, 1, 2....!!!"
    print(pengguna)
    print("=====================================================")
    sys.exit() # program dimatikan

# Menampilkan hasil variabel indeksKomputer
print("Komputer memilih :", komputer)

# Menampilkan hasil variabel indeksPengguna
print("Anda memilih :", pengguna)

# Menentukan pemenang
if komputer == pengguna :
    print("Draw.... Tidak ada pemenang")
elif (pengguna == "Gunting" and komputer == "Batu"):
    print("Anda kalah....!!! \n",
    "Komputer menang...!!!")
elif (pengguna == "Gunting" and komputer == "Kertas"):
    print("Anda menang....!!! \n",
    "Komputer kalah...!!!")
elif (pengguna == "Batu" and komputer == "Gunting"):
    print("Anda kalah....!!! \n",
    "Komputer menang...!!!")
elif (pengguna == "Batu" and komputer == "Kertas"):
    print("Anda menang....!!! \n",
    "Komputer kalah...!!!")
elif (pengguna == "Kertas" and komputer == "Gunting"):
    print("Anda kalah....!!! \n",
    "Komputer menang...!!!")
elif (pengguna == "Kertas" and komputer == "Batu"):
    print("Anda kalah....!!! \n",
    "Komputer menang...!!!")
else:
    pengguna = "Indeks hanya boleh diinput bilangan 0, 1, 2....!!!"
    print(pengguna)
    print("=====================================================")
    sys.exit() # program dimatikan

print("========================================================")