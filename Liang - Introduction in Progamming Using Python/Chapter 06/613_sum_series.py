# define number sequences
def numberSequence(i):
    mi = i / (i + 1)
    return mi

# define main function
def main():
    numberSeries = 0
    print("===============================================")
    print("||", format("i", "2s"), "|", format("m(i)", "6s"), "||")
    print("-----------------------------------------------")
    for n in range(1, 21):
        # count sum of sequence number
        numberSeries += numberSequence(n)
        print("||", format(n, "2d"), "|", format(numberSeries, "6.3f"), "||")
    print("===============================================")

# invoke main function
main()