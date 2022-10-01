# define Future Investment Value
def futureInvestmentValue(investmentAmount1, AnnualInterest1, years):
    futureValue = investmentAmount1 * (1 + AnnualInterest1 / 100) ** years
    return futureValue

# define main function
def main():
    investmentAmount2 = eval(input("The amount invested : "))
    AnnualInterest2 = eval(input("Annual interest rate : "))
    print("=======================================")
    print("||", format("Years", "5s"), "|", format("Future Value", "12s"), "||")
    print("---------------------------------------")
    for i in range(1, 31):
        print("||", format(i,"5d"), "|", format(futureInvestmentValue(investmentAmount2, AnnualInterest2, i), "12.2f"),"||")
    print("---------------------------------------")

main()