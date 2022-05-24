# =====================================
# Menggambar Bangun Datar Sederhana
# =====================================

import turtle

# 1. Setting pena
# 1a Ketebalan pena 3 px
turtle.pensize(3)

# 2. Menggambar segitiga
#2a Posisi pena ke atas 
turtle.penup()

# 2b Memindahkan pena 
turtle.goto(-200,-50)

# 2c Posisi pena ke bawah
turtle.pendown()

# 2d menggambar segitiga
turtle.circle(40, steps = 3)

# 3. Menggambar segiempat
# 3a Posisi pena ke atas 
turtle.penup()

# 3b Memindahkan pena 
turtle.goto(-100,-50)

# 3c Posisi pena ke bawah
turtle.pendown()

# 3d menggambar segitiga
turtle.circle(40, steps = 4)

# 4. Menggambar Segilima beraturan
# 4a Posisi pena ke atas 
turtle.penup()

# 4b Memindahkan pena 
turtle.goto(0,-50)

# 4c Posisi pena ke bawah
turtle.pendown()

# 4d menggambar segilima
turtle.circle(40, steps = 5)

# 5. Menggambar Segienam beraturan
# 5a Posisi pena ke atas 
turtle.penup()

# 5b Memindahkan pena 
turtle.goto(100,-50)

# 5c Posisi pena ke bawah
turtle.pendown()

# 5d menggambar segienam
turtle.circle(40, steps = 6)

# 6. Menggambar lingkaran
# 6a Posisi pena ke atas 
turtle.penup()

# 6b Memindahkan pena 
turtle.goto(200,-50)

# 6c Posisi pena ke bawah
turtle.pendown()

# 6d menggambar segienam
turtle.circle(40)

turtle.done()