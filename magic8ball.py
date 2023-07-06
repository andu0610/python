import turtle
import tkinter as tk
import random
mesaje: list[str]=['yes','no', 'probably}','idk']


screen=turtle.Screen()
screen.setup(500,800)
screen.bgcolor('green')
# screen.tracer(0)

timmy=turtle.Turtle()
timmy.shape('turtle')
timmy.color('white')


timmy.penup()
timmy.goto(-200,0)
timmy.pendown()
timmy.fillcolor('black')
timmy.begin_fill()
timmy.right(90)
timmy.circle(200)
timmy.end_fill()

timmy.penup()
timmy.goto(-100,0)
timmy.pendown()
timmy.fillcolor('#C0C0C0')
timmy.begin_fill()
timmy.circle(100)
timmy.end_fill()

timmy.penup()
timmy.goto(-75,-40)
timmy.pendown()
timmy.fillcolor('#006633')
timmy.begin_fill()
timmy.left(90)
timmy.forward(150)
timmy.left(120)
timmy.forward(150)
timmy.left(120)
timmy.forward(150)
timmy.end_fill()

matt=turtle.Turtle()
def generate():
     global matt
     matt.clear()
     matt=turtle.Turtle()
     matt.color('white')
     matt.penup()
     matt.setpos(250,0)
     matt.pendown()
     matt.write(random.choice(mesaje))



canvas=screen.getcanvas()
button=tk.Button(canvas.master, text="generate", command=generate)
button.pack()
button.place(x=245,y=650)
screen.mainloop()