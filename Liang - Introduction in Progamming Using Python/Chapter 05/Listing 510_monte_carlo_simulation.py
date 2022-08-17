import random

NUMBER_OF_TRIALS = 1000
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x ** 2 + y ** 2 <= 1:
        numberOfHits += 1
        print("----------------------------------")
        print("Titik (", x, ",", y,")")
        pi = 4 * numberOfHits / NUMBER_OF_TRIALS
        print("PI is", pi)

print("=================================")        
pi = 4 * numberOfHits / NUMBER_OF_TRIALS
print("PI is", pi)
print("=================================")
