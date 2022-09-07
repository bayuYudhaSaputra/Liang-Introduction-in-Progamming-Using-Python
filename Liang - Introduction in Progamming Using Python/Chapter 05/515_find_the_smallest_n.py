n = 1

print("--------------------------------------")
print("|", format("n","5s"), "|", format("n ^ 3", "5s"), "|")
print("--------------------------------------")

while n ** 3 < 12000:
    print("|", format(n,"5d"), "|", format(n ** 3, "5d"), "|")
    n += 1

print("--------------------------------------")

# n terbesar adalah n sebelum ditambahkan 1
print("Nilai n terbesar agar n ^ 3 < 12000 adalah n = ", n - 1 )