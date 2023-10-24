import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
canvas=tk.Canvas(root,width=500,height=500)
canvas.pack()

def on_button_click():
    name=tk.Label(canvas,text="cum te numesti?")
    name.pack()
    nume=tk.Text(root,height=5,width=10)
    nume.pack()
def intro():
    nume=entry_name.get()
    messagebox.showinfo("salut!",f"ok,{nume}! o sa ne jucam spanzuratoarea!")   

butonstart=tk.Button(canvas, text="start",height=10, width=50, command=on_button_click)

butonstart.pack()





# canvas.create_line(100,0,100,100, width=1, tags="aaa")
# canvas.create_line(100,100,0,100, width=1, tags="aaa")



root.mainloop()