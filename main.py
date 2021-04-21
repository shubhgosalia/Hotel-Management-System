from tkinter import *
from PIL import ImageTk, Image

# -----------splash_screen-----------------
sroot = Tk()
sroot.minsize(height=516, width=1150)
sroot.configure(bg='white')
Frame(sroot, height=516, width=5, bg='black').place(x=220, y=0)
Label(sroot, text="Hotel Management System ", font='Timesnewroman 40 ',
      bg='white', fg='black').place(x=235, y=30)
Label(sroot, text="Made by -", font='Timesnewroman 40 ',
      bg='white', fg='black').place(x=235, y=110)
Label(sroot, text="Shubh Gosalia - 1911015", font='Timesnewroman 40 ',
      bg='white', fg='grey').place(x=235, y=200)
Label(sroot, text="Meet Gajra - 1911011", font='Timesnewroman 40',
      bg='white', fg='grey').place(x=235, y=290)


def showHotel_status():
    pass


def showRooms():
    pass


def showStaff():
    pass


def reserve():
    pass


def mainroot():
    root = Tk()
    root.geometry('1080x500')
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg='white')
    root.title("Hotel Management System")
    top_frame = Frame(root, height=70, width=1080, bg='orange')
    top_frame.place(x=0, y=0)
    tf_label = Label(top_frame, text='Hotel Management System',
                     font='msserif 33', fg='black', bg='gray89', height=70)
    tf_label.pack(anchor='center')
    top_frame.pack_propagate(False)

    # ---------------NAV MENU--------------------------------------------------
    sl_frame = Frame(root, height=130, width=1080, bg='white')
    sl_frame.place(x=0, y=70+6)

    path1 = "images/hotelstatus.png"
    img1 = ImageTk.PhotoImage(Image.open(path1))
    b1 = Button(sl_frame, image=img1, text='b2',
                bg='white', width=180, command=showHotel_status)
    b1.image = img1
    b1.place(x=50, y=0)

    path2 = "images/rooms.png"
    img2 = ImageTk.PhotoImage(Image.open(path2))
    b2 = Button(sl_frame, image=img2, text='b1',
                bg='white', width=180, command=showRooms)
    b2.image = img2
    b2.place(x=230, y=0)

    path3 = 'images/Bookroom.png'
    img3 = ImageTk.PhotoImage(Image.open(path3))
    b3 = Button(sl_frame, image=img3, text='b2', bg='white',
                width=180, height=100, command=reserve)
    b3.image = img3
    b3.place(x=410, y=0)

    path4 = 'images/guests.png'
    img4 = ImageTk.PhotoImage(Image.open(path4))
    b4 = Button(sl_frame, image=img4, text='b2',
                bg='white', width=180, command=showStaff)
    b4.image = img4
    b4.place(x=590, y=0)

    path5 = 'images/logout.png'
    img5 = ImageTk.PhotoImage(Image.open(path5))
    b5 = Button(sl_frame, image=img5, text='b2', bg='white',
                width=180, height=100)
    b5.image = img5
    b5.place(x=770, y=0)

    Label(sl_frame, text='Hotel Status',
          font='msserif 13', bg='white').place(x=95, y=106)
    Label(sl_frame, text='Rooms', font='msserif 13',
          bg='white').place(x=290, y=106)
    Label(sl_frame, text='Reserve', font='msserif 13',
          bg='white').place(x=457, y=106)
    Label(sl_frame, text='Contacts', font='msserif 13',
          bg='white').place(x=644, y=106)
    Label(sl_frame, text='Exit', font='msserif 13',
          bg='white').place(x=858, y=106)
    sl_frame.pack_propagate(False)


def call_mainroot():
    sroot.destroy()
    mainroot()


sroot.after(10, call_mainroot)
mainloop()
