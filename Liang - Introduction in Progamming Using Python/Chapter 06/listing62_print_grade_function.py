# mendefinisikan fungsi untuk mencetak grade
def GradeFunction(score):
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')
    
# mendefinisikan fungsi main
def main():
    score = eval(input("Enter a score: "))
    print("The grade is ", end = " ")
    GradeFunction(score)

# memanggil fungsi main
main()