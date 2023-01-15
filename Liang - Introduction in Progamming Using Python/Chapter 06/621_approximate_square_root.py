# ==============================================================
# Memperkirakan hasil akar kuadrat menggunakan metode Babylonia
# ==============================================================

def sqrt(n):

    lastGuess = 1
    # diberi nilai awal 1
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    # rumus aproksimasi akar babylonia

    while (nextGuess - lastGuess > 0.000000001):
    # ketika selisih nextGuess dengan lastGuess lebih dari 0.000000001
    # hitung nextGuess hingga tidak memenuhi syarat.
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        lastGuess += 1

    return nextGuess

def main():
    n = eval(input("Input bilangan yang akan diakar : "))
    print("Akar dari", n, "adalah :", sqrt(n))

main()