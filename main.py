from tkinter import *

# -----------splash_screen-----------------
sroot = Tk()
sroot.minsize(height=516, width=1150)
sroot.configure(bg='white')
Frame(sroot, height=516, width=5, bg='black').place(x=220, y=0)
Label(sroot, text="Hotel Management System ", font='Timesnewroman 40 ',
      bg='white', fg='black').place(x=235, y=30)
Label(sroot, text="Made by -", font='Timesnewroman 40 ',
      bg='white', fg='black').place(x=235, y=110)
Label(sroot, text="Shubh Gosalia", font='Timesnewroman 40 ',
      bg='white', fg='grey').place(x=235, y=200)
Label(sroot, text="Meet Gajra", font='Timesnewroman 40',
      bg='white', fg='grey').place(x=235, y=290)


def mainroot():
    root = Tk()
    root.geometry('1080x500')
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg='white')
    root.title("Hotel Management System")


def call_mainroot():
    sroot.destroy()
    mainroot()


sroot.after(2000, call_mainroot)
mainloop()
