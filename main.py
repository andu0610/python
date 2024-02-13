import tkinter
from tkinter import messagebox


window=tkinter.Tk()
window.title("login form")
window.geometry("340x440")
window.configure(bg="#2e7058")

def login():
    username="andu"
    password="12345"
    if username_entry.get()==username and password_entry.get()==password and confirmPassword_entry.get()==password_entry.get():
        messagebox.showinfo(title="login success", message="ai intrat")
    else:
        messagebox.showinfo(title="error", message="n ai intrat")


frame=tkinter.Frame(window, bg="#b17058")

login_label=tkinter.Label(frame, text="login", bg="#b17014", fg="white", font=("Arial", 30))
username_label=tkinter.Label(frame, text="username", bg="#b1ff14", fg="white", font=("Arial", 20))
username_entry=tkinter.Entry(frame, font=("Arial", 20))

password_entry=tkinter.Entry(frame, show="*", font=("Arial", 20))
password_label=tkinter.Label(frame, text="password", bg="#b1ff14", fg="white", font=("Arial", 20))


login_button=tkinter.Button(frame, text="login", bg="#b1ff14", fg="white", font=("Arial", 20), command=login)

confirmPassword_entry=tkinter.Entry(frame, show="*", font=("Arial", 20))
confirmPassword_label=tkinter.Label(frame, text="confirm password", bg="#b1ff14", fg="white", font=("Arial", 20))

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
confirmPassword_label.grid(row=3, column=0)
confirmPassword_entry.grid(row=3, column=1, pady=20)

login_button.grid(row=4, column=0, columnspan=2, pady=20)


frame.pack()
window.mainloop()
