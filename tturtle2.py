import turtle
timmy=turtle.Turtle()
def up():
    timmy.forward(20)
def right():
    timmy.right(90)
def left():
    timmy.left(90)
ok=0
def jump():
    global ok
    if ok%2==0:
        timmy.penup()
    if ok%2==1:
        timmy.pendown()
    ok=ok+1
    
timmy.speed(50)
timmy.shape('turtle')

turtle.onkey(up, "Up")
turtle.onkey(right, "Right")
turtle.onkey(left,"Left")
turtle.onkey(jump,"space")
turtle.listen()

turtle.mainloop()