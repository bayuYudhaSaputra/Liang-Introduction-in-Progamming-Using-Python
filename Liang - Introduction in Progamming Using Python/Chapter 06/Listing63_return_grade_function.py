# mendefinisikan fungsi untuk mencetak grade
def getGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'E'

# Mendefinisikan fungsi pemanggil (caller) dengan nama main
def main():
    score = eval(input("Enter a score: "))
    print("The grade is ", getGrade(score))

# memanggil fungsi main
main()