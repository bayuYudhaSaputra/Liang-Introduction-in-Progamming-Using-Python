# ==================================================
# Listing 1.4.02
# ==================================================

# Mengimpor Turtle
import turtle

# Memindahkan titik acuan dari (0,0) ke (0,50)
turtle.goto(0,50)

# Mengarahkan garis ke atas
turtle.penup()

# Mengarahkan garis ke titik (50,-50)
turtle.goto(50,-50)

# Mengarahkan garis ke bawah
turtle.pendown()

# Mengubah warna garis menjadi merah
turtle.color("red")

# Membuat lingkaran
turtle.circle(50)