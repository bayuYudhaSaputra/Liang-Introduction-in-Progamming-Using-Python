# ========================================
# Turtle menggunakan warna
# ========================================

import turtle
turtle.pensize(3)

# 1. Menggambar Segitiga Berwarna Merah
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps = 3)
turtle.end_fill()

# 2. Menggambar Segiempat Berwarna Biru
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(40, steps = 4)
turtle.end_fill()

# 3. Menggambar Segilima Berwarna Hijau
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(40, steps = 5)
turtle.end_fill()

# 4. Menggambar Segienam Berwarna Kuning
turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(40, steps = 6)
turtle.end_fill()

# 5. Menggambar Lingkaran Berwarna Ungu
turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(40)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.write("Cool Colorful Shapes",
            font = ("Times", 18,"bold")
            )
turtle.hideturtle()
turtle.done()