# Define tax for single
def singleTax(income):
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + \
            (income - 8350) * 0.15    
    elif income <= 82250:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + \
            (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + \
            (171550 - 82250) * 0.28 + \
            (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + \
            (171550 - 82250) * 0.28 + \
            (372950 - 171550) * 0.33 + \
            (income - 372950) * 0.35    
    return tax

# Define tax for married jointly
def marriedJointlyTax(income):
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + \
            (income - 16700) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + \
            (67900 - 16700) * 0.15 + \
            (income - 67900) * 0.25
    elif income <= 208850:
        tax = 16700 * 0.10 + \
            (67900 - 16700) * 0.15 + \
            (137050 - 67900) * 0.25 + \
            (income - 137050) * 0.28
    elif income <= 372950:
        tax = 16700 * 0.10 + \
            (67900 - 16700) * 0.15 + \
            (137050 - 67900) * 0.25 + \
            (208850 - 137050) * 0.28 + \
            (income - 208850) * 0.33
    else:
        tax = 16700 * 0.10 + \
            (67900 - 16700) * 0.15 + \
            (137050 - 67900) * 0.25 + \
            (208850 - 137050) * 0.28 + \
            (372950 - 208850) * 0.33 + \
            (income - 372950) * 0.35
    return tax

# Define tax for married separately
def marriedSeparatelyTax(income):
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + \
            (income - 8350) * 0.15
    elif income <= 68525:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 104425:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + \
            (income - 68525) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + \
            (104425 - 68525) * 0.28 + \
            (income - 104425) * 0.33
    else:
        tax = 8350 * 0.10 + \
            (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + \
            (104425 - 68525) * 0.28 + \
            (372950 - 104425) * 0.33 + \
            (income - 372950) * 0.35
    return tax

# Define tax for Head of House Hold
def headOfHouseHoldTax(income):
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + \
            (income - 11950) * 0.15
    elif income <= 117450:
        tax = 11950 * 0.10 + \
            (45500 - 11950) * 0.15 + \
            (income - 45500) * 0.25
    elif income <= 104425:
        tax = 11950 * 0.10 + \
            (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + \
            (income - 117450) * 0.28
    elif income <= 190200:
        tax = 11950 * 0.10 + \
            (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + \
            (104425 - 117450) * 0.28 + \
            (income - 104425) * 0.33
    else:
         tax = 11950 * 0.10 + \
            (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + \
            (104425 - 117450) * 0.28 + \
            (190200 - 104425) * 0.33 + \
            (income - 190200) * 0.35
    return tax

# Define compute tax
def computeTax(status, taxableIncome):
    if status == 1: # jika status = 1
        return format(singleTax(taxableIncome),"16.2f")
        # mengembalikan nilai fungsi singleTax()

    elif status == 2: # jika status = 2
        return format(marriedJointlyTax(taxableIncome), "16.2f")
        # mengembalikan nilai fungsi marriedJointlyTax()

    elif status == 3: # jika status = 3
        return format(marriedSeparatelyTax(taxableIncome), "16.2f")
        # mengembalikan nilai fungsi marriedSeparatelyTax()

    elif status == 4: # jika status = 4
        return format(headOfHouseHoldTax(taxableIncome), "16.2f")
        # mengembalikan nilai fungsi marriedSeparatelyTax()


# Define main
def main():
    print("===============================================================================================================================")
    print("||", format("Taxable Income","16s"), "|", format("Single", "16s"), "|", format("Married Joint", "16s"), "|", format("Married Separate", "16s"), "|", format("Head of a House", "16s"), "||")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    for i in range(50000, 60000, 50):
        print("||", format(i, "16.2f"), "|",computeTax(1, i), "|", computeTax(2, i), "|", computeTax(3, i), "|", computeTax(4, i), "||")
    print("===============================================================================================================================")

main()