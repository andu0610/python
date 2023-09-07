from tkinter import *
import random
width=500
height=500
speed=200
space_size=20
snake="#1fe090"
food="#c9b536"
background="black"

class Snake:
    def __init__(self):
        self.body_size=BODY_SIZE
        self.coordinates=[]
        self.squares=[]
        
        for i in range(0,BODY_SIZE):
            self.coordinates.append([0,0])
            
        for x,y in self.coordinates:
            square=canvas.create_rectangle(
                x,y,x+space_size, Y+space_size, fill=snake, tag='snake')
            self.squares.append(square)
            
class Food:
    def __init__(self):
        x=random.randint(0,(width/space_size)-1)*space_size
        y=random.randint(0, (height/space_size)-1)*space_size
        
        self.cordinates=[x,y]
        canvas.create_oval(x,y,x + space_size,y+ space_size, fill=food, tag="food")
        
def next_turn(snake, food):
    pass



def change_direction(new_direction):
    global direction
    if new_direction=='left':
        if direction!='right':
            direction=new_direction
    elif new_direction=='right':
        if direction!='left':
            direction=new_direction
    elif new_direction=="up":
        if direction!='down':
            direction=new_direction
    elif new_direction=='down':
        if direction!='up':
            direction=new_direction
         

def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=width:
        return True
    elif y<0 or y>=height:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1:]:
            return True
        
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                  canvas.winfo_height()/2,
                  font=('consolas', 70),
                  text='GAME OVER', fill='red',
                  tag='gameover')
    
window=Tk()
window.title('Snake Game')

score=0
direction='down'

label=Label(window, text='Points:{}'.format(score),font=('consolas', 20))

label.pack()

canvas=Canvas(window, bg=background, height=height, width=width)
canvas.pack()

window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))

window.geomwtry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('left')
