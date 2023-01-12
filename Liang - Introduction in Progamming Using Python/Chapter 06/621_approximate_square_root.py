# ==============================================================
# Memperkirakan hasil akar kuadrat menggunakan metode Babylonia
# ==============================================================

n = 5
lastGuess = 1
nextGuess = (lastGuess + (n / lastGuess)) / 2

print("|", "lastGuess", "|", "nextGuess", "|")
while (nextGuess - lastGuess > 0.000000001):
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    print("|", lastGuess, "|", nextGuess, "|")
    lastGuess += 1
