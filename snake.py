import turtle
import random
import time


WIDTH=500
HEIGHT=500
SPACE_SIZE=20
SNAKE="green"
FOOD="white"
BACKGROUND="black"

wn=turtle.Screen()
wn.title("Turtle Snake Game")
wn.bgcolor(BACKGROUND)
wn.setup(width= WIDTH, height=HEIGHT)

snake_head=turtle.Turtle()
snake_head.speed(1)
snake_head.shape("square")
snake_head.color(SNAKE)
snake_head.penup()
x=random.randint(-WIDTH/2+SPACE_SIZE, WIDTH/2-SPACE_SIZE)
y=random.randint(-HEIGHT/2+SPACE_SIZE, HEIGHT/2-SPACE_SIZE)
snake_head.goto(x, y)
snake_head.direction="Stop"
def create_food():
    x=random.randint(-WIDTH/2+SPACE_SIZE, WIDTH/2-SPACE_SIZE)
    y=random.randint(-HEIGHT/2+SPACE_SIZE, HEIGHT/2-SPACE_SIZE)
    food.goto(x,y)
food=turtle.Turtle()
food.speed(0)
food.shape('turtle')
food.color(FOOD)
food.penup()
create_food()

snake_body=[]

def move():
    if snake_head.direction=="up":
        y=snake_head.ycor()
        snake_head.sety(y+SPACE_SIZE)
        
    if snake_head.direction=="down":
        y=snake_head.ycor()
        snake_head.sety(y-SPACE_SIZE)
        
    if snake_head.direction=="right":
        x=snake_head.xcor()
        snake_head.sety(x+SPACE_SIZE)
        
    if snake_head.direction=="left":
        x=snake_head.xcor()
        snake_head.sety(x-SPACE_SIZE)
        
        
def go_up():
    if snake_head.direction !="down":
        snake_head.direction="up"
        
def go_down():
    if snake_head.direction !="up":
        snake_head.direction="down"
        
def go_right():
    if snake_head.direction !="left":
        snake_head.direction="right"
        
def go_left():
    if snake_head.direction !="right":
        snake_head.direction="left"
        
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

while True:
    wn.update()
    move()
    
    if snake_head.distance(food)<20:
        create_food()
        
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        snake_body.append(new_segment)
        new_segment.speed(1)
        new_segment.shape("square")
        new_segment.color(SNAKE)
        new_segment.penup()
    
    #moving the segments of the snake s body    
    for i in range(len(snake_body)-1, 0, -1):
        x=snake_body[i-1].xcor()
        y=snake_body[i-1].ycor()
        snake_body[i].goto(x,y)
    
    if len(snake_body)>0:
        x=snake_head.xcor()
        y=snake_head.ycor()
        snake_body[0].goto(x,y)
    
    
    time.sleep(0.1)
    
wn.mainloop()