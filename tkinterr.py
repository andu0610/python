import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.root=tk.Tk()

        self.label=tk.Label(self.root, text="message", font=("Arial", 16))
        self.label.pack(padx=10, pady=10)

        self.textbox=tk.Text(self.root, height=3, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10,pady=10)

        self.checkstate=tk.IntVar()

        self.check=tk.Checkbutton(self.root, text="show message box", font=("Arial", 16), variable=self.checkstate)
        self.check.pack(padx=10, pady=10)

        self.btn=tk.Button(self.root, text="show message", font=("Arial", 16), command=self.showMessage)
        self.btn.pack(padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.onclosing)
        self.root.mainloop()

    def showMessage(self):
        if self.checkstate.get()==0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="message", message=self.textbox.get("1.0", tk.END))

    def shortcut(self, event):
        # print(event)
        # print(event.keysim)
        # print(event.state)
        # if event.state==4 and event.keysym=="Return":
        #     print("hello")
        #     self.showMessage()

    def onclosing(self):
        if messagebox.askyesno(title="Quit?", message="do you really want to quit?"):
            self.root.destroy()

MyGUI()

