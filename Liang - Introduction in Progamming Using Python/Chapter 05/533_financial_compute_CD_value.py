print("\n========================================")
deposito = eval(input("Berapa nominal deposito yang disimpan? Rp."))
bungaPersen = eval(input("Berapa persen bunga tahunan yang didapat? "))
jangkaWaktu = eval(input("Berapa bulan jangka waktu deposito? "))

print("\n---------------------------------------")
print("|", format("Bulan ke","8s"), "|", format("Nilai Deposito","10s"), "|")
print("---------------------------------------\n")

if deposito <= 0 or bungaPersen <= 0 or jangkaWaktu <= 0:
    print("Deposito, bunga dan jangka waktu harus bilangan positif")
else:
    for i in range(1, jangkaWaktu + 1):
        bungaNominal = deposito * (bungaPersen / 1200)
        deposito += bungaNominal
        print("|", format(i,"8.0f"), "|", format(deposito,"14.2f"), "|")

print("---------------------------------------\n")