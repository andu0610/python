
import tkinter
import random
colours=['red','blue','green','pink','black','yellow','orange','white','purple','brown']
score=0
timeleft=5

def startgame(event):
    if timeleft==5:
        countdown()
    nextcolour()
    
def nextcolour():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score +=1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text='score:'+str(score))
        
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timeLabel.config(text='Time left:'
                         +str(timeleft))   
        timeLabel.after(1000, countdown) 
    if timeleft==0:
        scoreLabel.destroy()
        timeLabel.destroy()
        instructions.destroy()
        label.destroy()
        e.destroy()
        endLabel=tkinter.Label(root,text='ai terminat cu '+str(score)+' puncte', font=('Times New Roman',30))
        endLabel.pack()
root=tkinter.Tk()
root.title('COLO0RGAME')
root.geometry('500x500')
instructions=tkinter.Label(root, text="scrie culoarea textului,"
                           "nu cuvantul",
                            font=('Times New Roman', 12))
instructions.pack()
scoreLabel=tkinter.Label(root, font=('Times New Roman',60))
scoreLabel.pack()
label=tkinter.Label(root, font=('Times New Roman', 60))
label.pack()
timeLabel=tkinter.Label(root, font=('Times New Roman', 60))
timeLabel.pack()
e=tkinter.Entry(root)
root.bind('<Return>', startgame)
e.pack()
e.focus_set()
root.mainloop()