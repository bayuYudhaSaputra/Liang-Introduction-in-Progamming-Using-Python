# Define commision value
def computeCommission(salesAmount):
    if salesAmount > 0.01 and salesAmount <= 5000:
        # Jika penjualan antara 0.01 hingga 5000
        commission = 0.08 * salesAmount
        # komisi 8%
        return commission
    elif salesAmount > 5000 and salesAmount <= 10000:
        # Jika penjualan antara 5000.01 hingga 10000
        commission = 0.1 * salesAmount
        # komisi 10%
        return commission
    elif salesAmount > 10000:
        # Jika penjualan lebih dari 10000
        commission = 0.12 * salesAmount
        # komisi 12%
        return commission
    else:
        statementError = "Invalid Sales Amount"
        return statementError

def main():
    print("====================================")
    print("||", format("Sales Amount", "14s"), "|", format("Commission", "12s"), "||")
    
    for salesAmount in range(10000, 100001, 5000):
        # perulangan mulai dari 10000 hingga 100001
        # dengan increment 5000
        print("------------------------------------")
        printCommission = computeCommission(salesAmount)
        print("||", format(salesAmount,"14.2f"), "|", format(printCommission,"12.2f"), "||")
    print("====================================")

main()