# define number sequence
def numberSequence(i):
    mi = ((-1) ** (i + 1)) / (2 * i - 1)
    return mi

# define main function
def main():
    numberSeries = 0
    print("===============================================")
    print("||", format("i", "2s"), "|", format("m(i)", "6s"), "||")
    print("-----------------------------------------------")
    for n in range(1, 1000, 100):
        # count sum of sequence number
        numberSeries += numberSequence(n)
        phi = 4 * numberSeries
        print("||", format(n, "2d"), "|", format(phi, "6.3f"), "||")
    print("===============================================")

main()