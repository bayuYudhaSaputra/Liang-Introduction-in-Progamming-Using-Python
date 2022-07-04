# =============================================================
# Menyatakan mata uang dolar dalam :
# - dolar
# - Cent
# - Quarter
# - Dime
# - Nickel
# - Pennies
# ===========================================================
 
print("===========================================================")
 
# Receive the amount
amount = eval(input("Enter an amount (for example, USD.11.56): USD."))
 
# Convert the amount to cents
remainingAmount = int(amount * 100)
 
# -----------------------------------------------------
# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100
 
# Display the results of one dollars
print("Your amount", amount, "consists of")
 
if numberOfOneDollars == 1:
   print("\t", numberOfOneDollars, "dollar")
else:
   print("\t", numberOfOneDollars, "dollars")
# -----------------------------------------------------
 
# -----------------------------------------------------
# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25
 
# Display the results of quarters
if numberOfQuarters == 1:
   print("\t", numberOfQuarters, "quarter")
else:
   print("\t", numberOfQuarters, "quarters")
# -----------------------------------------------------
 
# -----------------------------------------------------
# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10
 
# Display the results of dimes
if numberOfDimes == 1:
   print("\t", numberOfDimes, "dime")
else:
   print("\t", numberOfDimes, "dimes")
# -----------------------------------------------------
 
# -----------------------------------------------------
# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5
 
# Display the results of dimes
if numberOfNickels == 1:
   print("\t", numberOfNickels, "nickel")
else:
   print("\t", numberOfNickels, "nickels")
# -----------------------------------------------------
 
 
# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount
 
# Display the results of dimes
if numberOfPennies == 1:
   print("\t", numberOfPennies, "pennie")
else:
   print("\t", numberOfPennies, "pennies")
# -----------------------------------------------------
 
print("===========================================================")