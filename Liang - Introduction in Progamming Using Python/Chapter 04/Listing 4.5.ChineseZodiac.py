year = eval(input("Enter a year : "))

zodiacYear = year % 12

if zodiacYear == 0:
    print(year, "is the year of the monkey.")
elif zodiacYear == 1:
    print(year, "is the year of the roaster.")
elif zodiacYear == 2:
    print(year, "is the year of the dog.")
elif zodiacYear == 3:
    print(year, "is the year of the pig.")
elif zodiacYear == 4:
    print(year, "is the year of the rat.")
elif zodiacYear == 5:
    print(year, " is the year of the ox.")
elif zodiacYear == 6:
    print(year, "is the year of the tiger.")
elif zodiacYear == 7:
    print(year, "is the year of the rabbit.")
elif zodiacYear == 8:
    print(year, "is the year of the dragon.")
elif zodiacYear == 9:
    print(year, "is the year of the snake.")
elif zodiacYear == 10:
    print(year, "is the year of the horse.")
else:
    print(year, "is the year of the sheep.")   