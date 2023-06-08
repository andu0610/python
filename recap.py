# class Persoana:
#     def __init__(self, varsta, nume):
#         self.varsta=varsta
#         self.nume=nume
    
#     def printpers(self):
#         print (self.varsta)
#         print (self.nume)
# pers=Persoana(16,"aaa")
# pers.printpers()

import tkinter as tk

# def changelabel():
#     aaa.config(text="efidv")

# def printare():
#     print("likhb")

# fereastra=tk.Tk()
# fereastra.geometry("500x500")
# aaa=tk.Label(text="sfv")
# aaa.pack()
# ccc=tk.Button(text="click me", command=changelabel)
# ccc.pack()

# tk.mainloop()

xsi0=tk.Tk()
xsi0.geometry("500x500")
# label1=tk.Label(text='X si 0')
# label1.pack()
def buttonclick0():
    a=input("X sau 0")
    button0.config(text=a)
def buttonclick1():
    a=input("X sau 0")
    button1.config(text=a)
def buttonclick2():
    a=input("X sau 0")
    button2.config(text=a)
def buttonclick3():
    a=input("X sau 0")
    button3.config(text=a)
def buttonclick4():
    a=input("X sau 0")
    button4.config(text=a)
def buttonclick5():
    a=input("X sau 0")
    button5.config(text=a)
def buttonclick6():
    a=input("X sau 0")
    button6.config(text=a)
def buttonclick7():
    a=input("X sau 0")
    button7.config(text=a)
def buttonclick8():
    a=input("X sau 0")
    button8.config(text=a)
            
            

button0=tk.Button(width=5, height=3, command=buttonclick0)
button1=tk.Button(width=5, height=3, command=buttonclick1)
button2=tk.Button(width=5, height=3, command=buttonclick2)
button3=tk.Button(text=" ", width=5, height=3, command=buttonclick3)
button4=tk.Button(text=" ", width=5, height=3, command=buttonclick4)
button5=tk.Button(text=" ", width=5, height=3, command=buttonclick5)
button6=tk.Button(text=" ", width=5, height=3, command=buttonclick6)
button7=tk.Button(text=" ", width=5, height=3, command=buttonclick7)
button8=tk.Button(text=" ", width=5, height=3, command=buttonclick8)

button0.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)
button5.grid(row=1, column=2)
button6.grid(row=2, column=0)
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
ok=False
tk.mainloop()
while ok==False:
    # if button0.cget('text')=="0" and button1.cget("text")=="0" and button2.cget('text')=="0" or button0.cget('text')=="X" and button1.cget("text")=="X" and button2.cget('text')=="X":
        # print(f"{button0.cget('text')} a castigat")
        # ok=True
    print(button0.cget('text'))
    print('x')


