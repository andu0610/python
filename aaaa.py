import tkinter as tk
import random
from tkinter import messagebox
def checkwinner(player, computer):
    if player==computer:
        if player=="pistol":
            return "ai pierdut"
        else:
            return "egalitate"
    elif player=="piatra" and computer=="foarfeca" or player=="foarfeca" and computer=="hartie" or player=="hartie" and computer=="piatra" or player=="pistol":
        return "ai castigat"
    else:
        return "ai pierdut"

def playgame(player):
    choices=['piatra', 'foarfeca', 'hartie', 'pistol']
    computer=random.choice(choices)
    result= checkwinner(player, computer)
    messagebox.showinfo('result', result)
def Fereastra():
    fereastra=tk.Tk()
    fereastra.geometry("500x500")
    aaa=tk.Label(text='piatra, foarfeca, hartie, pistol: ')
    aaa.grid(row=0, column=0)
    piatra=tk.Button(text="piatra", command=lambda: playgame("piatra"))
    piatra.grid(row=0, column=1)
    foarfeca=tk.Button(text="foarfeca", command=lambda: playgame("foarfeca"))
    foarfeca.grid(row=0, column=2)
    hartie=tk.Button(text="hartie", command=lambda: playgame("hartie"))
    hartie.grid(row=0, column=3)
    pistol=tk.Button(text="pistol", command=lambda: playgame("pistol"))
    pistol.grid(row=0, column=4)
    
Fereastra()
tk.mainloop()

