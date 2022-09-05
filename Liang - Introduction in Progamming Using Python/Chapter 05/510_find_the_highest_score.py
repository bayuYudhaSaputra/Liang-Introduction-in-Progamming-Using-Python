f = open('Liang - Introduction in Progamming Using Python/Chapter 05/score.txt','r')
# membuka file dengan nama score.txt
for line in f:
# membaca isi file dengan nama score.txt
    isiFile = int(line)
    nilaiMaks = 0
    print(isiFile)
   

f.close()
# menutup file dengan nama score.txt