# define number sequence
def numberSequence(i):
    ui = ((-1) ** (i + 1)) / (2 * i - 1)
    return ui

# define number series to estimate the value of phi
def numberSeriesPhi(j):
    numberSeries = 0
    for j in range(1, j + 1):
        numberSeries += numberSequence(j)
        mi = 4 * numberSeries
        return mi

# define main function
def main():
    print("===============================================")
    print("||", format("i", "3s"), "|", format("m(i)", "6s"), "||")
    print("-----------------------------------------------")
    for n in range(1, 1000, 100):
        print("||", format(n, "3d"), "|", format(numberSeriesPhi(n), "6.4f"), "||")
    print("===============================================")

main()