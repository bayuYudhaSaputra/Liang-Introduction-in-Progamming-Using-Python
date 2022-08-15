year = 0
tuition = 10000 # tuition in year 0

while tuition < 20000:
    year += 1
    tuition *= 1.07

print("Tuition will be doubled in", year, "years")
print("Tuition will be $" + format(tuition, ".2f"),
    "in", year, "years")