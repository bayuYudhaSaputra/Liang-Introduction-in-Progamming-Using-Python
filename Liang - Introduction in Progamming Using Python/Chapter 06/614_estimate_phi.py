# define number sequence
def numberSequence(i):
    ui = ((-1) ** (i + 1)) / (2 * i - 1)
    return ui

# define main function
def main():
    numberSeries = 0
    print("===============================================")
    print("||", format("i", "3s"), "|", format("m(i)", "6s"), "||")
    print("-----------------------------------------------")
    for n in range(1, 1000, 100):
        # count sum of sequence number
        numberSeries += numberSequence(n)
        mi = 4 * numberSeries
        print("||", format(n, "3d"), "|", format(mi, "6.3f"), "||")
    print("===============================================")

main()