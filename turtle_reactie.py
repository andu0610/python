import tkinter as tk
import time
import random

def startjoc():
    canvas.itemconfig(red_dot, fill="red")
    root.after(random.randint(1000, 5000), turn_bluegreen)

def turn_bluegreen():
    list1=[1,2,3,4,5,6,7,8,9,10]
    while len(list1)!=0:
        x=random.choice(list1)
        list1.remove(x)
        if x>3:
                canvas.itemconfig(red_dot, fill="blue")
                time.sleep(3)
        else:
            global starttime
            canvas.itemconfig(red_dot, fill="green")
            starttime=time.time()
            time.sleep(3)

# def turngreen():
#     global starttime
#     canvas.itemconfig(red_dot, fill="green")
#     starttime=time.time()

def on_click(event):
    if canvas.itemcget(red_dot, 'fill')=='green':
        reaction_time=time.time()-starttime
        show_reaction_time(reaction_time)
    else: 
        canvas.delete(red_dot)
        canvas.create_text(200,200,
                        text=f"ai pierdut",
                        fill="black",
                        font=("Times New Roman", 20)
                        )                   
def show_reaction_time(reaction_time):
    canvas.delete(red_dot)
    canvas.create_text(200,200,
                        text=f"Timp de reactie:{reaction_time:.3f} secunde",
                        fill="black",
                        font=("Times New Roman", 20)
                        )                   
    # root.after(3000, startjoc())


root=tk.Tk()
root.title('test de reactie')
root.geometry('400x400')
canvas=tk.Canvas(root, width=400, height=400,bg='white')
canvas.pack()
red_dot=canvas.create_oval(150, 150, 250, 250, fill='red')
canvas.bind("<Button-1>", on_click)

startjoc()
root.mainloop()