import random
# ===========================================
# Permainan Lotere
# ===========================================

noLotre = random.randint(100,999)
# Ekstrak no Lotre
noLotreRatusan = noLotre // 100
sisaNoLotreRatusan = noLotre % 100
# -----------------------------------------------
noLotrePuluhan = sisaNoLotreRatusan // 10
# -----------------------------------------------
noLotreSatuan = sisaNoLotreRatusan % 10
# -----------------------------------------------

tebakan = eval(input("Input nomor lotre yang terdiri dari 3 digit (misal 568) : "))
# Ekstrak tebakan 
tebakanRatusan = tebakan // 100
sisaRatusan = tebakan % 100
# -----------------------------------------------
tebakanPuluhan = sisaRatusan // 10
# -----------------------------------------------
tebakanSatuan = sisaRatusan % 10
# -----------------------------------------------


print("angka lotere yang muncul adalah :", noLotre)
# ketiga bilangan dan urutan tepat
if tebakan == noLotre:
    print("Tebakan anda tepat : Anda mendapat USD 10.000")
# ketiga bilangan tepat tetapi urutannya tidak tepat
elif (noLotreRatusan == tebakanPuluhan and \
    noLotreRatusan == tebakanSatuan and \
    noLotrePuluhan == tebakanRatusan and \
    noLotrePuluhan == tebakanSatuan and \
    noLotreSatuan == tebakanRatusan and \
    noLotreSatuan == tebakanPuluhan
    ):
    print("Tebakan angka anda tepat tetapi urutannya tidak tepat : Anda mendapat USD 3.000")
# ada tepat satu digit yang sama
elif (noLotreRatusan == tebakanRatusan or \
    noLotreRatusan == tebakanPuluhan or \
    noLotreRatusan == tebakanSatuan or \
    noLotrePuluhan == tebakanRatusan or \
    noLotrePuluhan == tebakanPuluhan or \
    noLotrePuluhan == tebakanSatuan or \
    noLotreSatuan == tebakanRatusan or \
    noLotreSatuan == tebakanPuluhan or \
    noLotreSatuan == tebakanSatuan 
    ):
    print("Hanya satu angka yang tepat : Anda mendapat hadian USD 1.000")
# ketiga bilangan tidak tepat
else:
    print("Maaf.. tebakan anda tidak ada yang tepat!!")