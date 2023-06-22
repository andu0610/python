import turtle

timmy=turtle.Turtle()
timmy.speed(50)
timmy.shape('turtle')


# timmy.forward(100)
# timmy.left(90)
# timmy.forward(30)
# timmy.left(90)
# timmy.forward(70)
# timmy.right(90)
# timmy.forward(200)
# timmy.left(90)
# timmy.forward(30)
# timmy.left(90)
timmy.penup()
timmy.goto(0,-100)
timmy.pendown()
for i in range(360):
    timmy.forward(1)
    timmy.left(1)
timmy.left(180)
timmy.penup()
timmy.forward(115)
timmy.pendown()
for i in range(360):
    timmy.forward(1)
    timmy.right(1)
timmy.right(90)
timmy.penup()
timmy.forward(115)
timmy.pendown()
timmy.forward(150)
for i in range(180):
    timmy.forward(1)
    timmy.right(1)
timmy.forward(150)
# timmy.left()

# timmy.setheading()
# timmy.speed()
# timmy.penup()
# timmy.pendown()

 
timmy.end_fill()












turtle.mainloop()