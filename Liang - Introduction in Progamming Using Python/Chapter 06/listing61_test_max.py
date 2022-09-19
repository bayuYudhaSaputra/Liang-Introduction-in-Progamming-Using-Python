# 01. mendefinisikan fungsi max untuk :
# 01.1. membandingkan dua bilangan yang lebih besar
def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result

# 02. Mendefinisikan fungsi main untuk :
# 02.1. memberi nilai untuk fungsi max
# 02.2. memanggil fungsi max
def main():
    i = 2
    j = 5
    k = max(i, j) # memanggil fungsi max
    print("The larger number of", i, "and", j, "is", k)

# 03. memanggil fungsi main
main()