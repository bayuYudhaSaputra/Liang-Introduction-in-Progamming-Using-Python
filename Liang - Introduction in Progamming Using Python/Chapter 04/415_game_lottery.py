import random
# ===========================================
# Permainan Lotere
# ===========================================

noLotre = random.randint(100,999)
# Ekstrak no Lotre
noLotreDigitRatusan = noLotre // 100
sisaNoLotreRatusan = noLotre % 100
# -----------------------------------------------
noLotreDigitPuluhan = sisaNoLotreRatusan // 10
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
if tebakan == noLotre:
    print("Tebakan anda tepat : Anda mendapat USD 10.000")
else:
    print("Maaf.. tebakan anda tidak ada yang tepat!!")