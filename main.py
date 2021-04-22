from tkinter import *
from PIL import ImageTk, Image

# -----------splash_screen-----------------
sroot = Tk()
sroot.minsize(height=516, width=1150)
sroot.configure(bg="white")
Frame(sroot, height=516, width=5, bg="black").place(x=220, y=0)
Label(
    sroot,
    text="Hotel Management System ",
    font="Timesnewroman 40 ",
    bg="white",
    fg="black",
).place(x=235, y=30)
Label(sroot, text="Made by -", font="Timesnewroman 40 ", bg="white", fg="black").place(
    x=235, y=110
)
Label(
    sroot,
    text="Shubh Gosalia - 1911015",
    font="Timesnewroman 40 ",
    bg="white",
    fg="grey",
).place(x=235, y=200)
Label(
    sroot, text="Meet Gajra - 1911011", font="Timesnewroman 40", bg="white", fg="grey"
).place(x=235, y=290)


def showRooms():
    pass


def reserve():
    pass


def mainroot():
    root = Tk()
    root.geometry("1080x500")
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg="white")
    root.title("Hotel Management System")
    top_frame = Frame(root, height=70, width=1080, bg="dark orange")
    top_frame.place(x=0, y=0)
    tf_label = Label(
        top_frame,
        text="Hotel Management System",
        font="msserif 33",
        fg="black",
        bg="gray89",
        height=70,
    )
    tf_label.pack(anchor="center")
    top_frame.pack_propagate(False)

    def showHotel_status():
        global b_frame
        b_frame = Frame(root, height=400, width=1080, bg="gray91")
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        path = "images/texture_bg.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        tor = 25
        rer = 15
        tos = 13
        avr = int(tor) - int(rer)
        avr = str(avr)

        hts = Label(
            b_frame,
            text="Hotel Status",
            font="msserif 15",
            fg="black",
            bg="gray91",
            height=1,
        )

        smf1 = Frame(b_frame, height=150, width=175, bg="white")
        tr = Label(
            smf1,
            text="Total Rooms:",
            fg="white",
            bg="red4",
            width=100,
            height=2,
            font="helvetica 15",
        )
        tr.pack(side="top")
        smf1.pack_propagate(False)
        smf1.place(x=0, y=30)
        Label(smf1, text=tor, fg="red4", bg="white", font="msserif 50").pack(
            anchor="center"
        )

        smf2 = Frame(b_frame, height=150, width=175, bg="white")
        ar = Label(
            smf2,
            text="Available Rooms:",
            fg="white",
            bg="red4",
            width=130,
            height=2,
            font="helvetica 15",
        )
        ar.pack(side="top")
        smf2.pack_propagate(False)
        smf2.place(x=180 + 4, y=30)
        Label(smf2, text=avr, fg="red4", bg="white", font="msserif 50").pack(
            anchor="center"
        )

        smf3 = Frame(b_frame, height=150, width=175, bg="white")
        tre = Label(
            smf3,
            text="Total reservations:",
            fg="white",
            bg="red4",
            width=130,
            height=2,
            font="helvetica 15",
        )
        tre.pack(side="top")
        smf3.pack_propagate(False)
        smf3.place(x=360 + 6, y=30)
        Label(smf3, text=rer, fg="red4", bg="white", font="msserif 50").pack(
            anchor="center"
        )

        smf4 = Frame(b_frame, height=150, width=175, bg="white")
        tc = Label(
            smf4,
            text="Total Customers:",
            fg="white",
            bg="red4",
            width=130,
            height=2,
            font="helvetica 15",
        )
        tc.pack(side="top")
        smf4.pack_propagate(False)
        smf4.place(x=540 + 8, y=30)
        Label(smf4, text="50", fg="red4", bg="white", font="msserif 50").pack(
            anchor="center"
        )

        smf5 = Frame(b_frame, height=150, width=175, bg="white")
        ts = Label(
            smf5,
            text="Total Staff:",
            fg="white",
            bg="red4",
            width=130,
            height=2,
            font="helvetica 15",
        )
        ts.pack(side="top")
        smf5.pack_propagate(False)
        smf5.place(x=720 + 10, y=30)
        Label(smf5, text=tos, fg="red4", bg="white", font="msserif 50").pack(
            anchor="center"
        )
        redf1 = Frame(b_frame, height=8, width=1080, bg="cyan4")

        smf6 = Frame(b_frame, height=150, width=175, bg="white")
        ts = Label(
            smf6,
            text="Under renovation:",
            fg="white",
            bg="red4",
            width=130,
            height=2,
            font="helvetica 15",
        )
        ts.pack(side="top")
        smf6.pack_propagate(False)
        smf6.place(x=915, y=30)
        Label(smf6, text="5", fg="red4", bg="white", font="msserif 50").place(
            x=60, y=60
        )

    def showStaff():
        b_frame = Frame(root, height=400, width=1080, bg="white")
        label = Label(b_frame, height=400, width=1080)
        label.place(x=0, y=0)

        emp1f = Frame(b_frame)
        path1 = "images/newman.jpg"
        img1 = ImageTk.PhotoImage(Image.open(path1))
        emp1 = Label(emp1f, image=img1)
        emp1.image = img1
        emp1.pack()
        emp1f.place(x=0, y=0)
        emp1inf = Frame(b_frame, bg="White", height=122, width=300)
        Label(emp1inf, text="Manager", bg="white", font="msserif 17 bold").place(
            x=60, y=0
        )
        Label(emp1inf, text="John Doe", bg="white", fg="Grey", font="msserif 10").place(
            x=60, y=37
        )
        Label(
            emp1inf, text="Phone : 999", bg="white", fg="Grey", font="msserif 10"
        ).place(x=60, y=59)
        Label(
            emp1inf,
            text="Mail : JohnDoe@google.com",
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=60, y=83)
        emp1inf.place(x=117, y=1)

        emp1f = Frame(b_frame)
        path2 = "images/receptionnew.jpg"
        img2 = ImageTk.PhotoImage(Image.open(path2))
        emp1 = Label(emp1f, image=img2)
        emp1.image = img2
        emp1.pack()
        emp1f.place(x=657, y=0)
        emp1inf = Frame(b_frame, bg="White", height=116, width=310)
        Label(emp1inf, text="Receptionist", bg="white", font="msserif 17 bold").place(
            x=45, y=0
        )
        Label(emp1inf, text="John Doe", bg="white", fg="Grey", font="msserif 10").place(
            x=45, y=37
        )
        Label(
            emp1inf, text="Phone : 999", bg="white", fg="Grey", font="msserif 10"
        ).place(x=45, y=59)
        Label(
            emp1inf,
            text="Mail : JohnDoe@google.com",
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=45, y=83)
        emp1inf.place(x=767, y=2)

        emp1f = Frame(b_frame)
        path3 = "images/fchefnew.jpg"
        img3 = ImageTk.PhotoImage(Image.open(path3))
        emp1 = Label(emp1f, image=img3)
        emp1.image = img3
        emp1.pack()
        emp1f.place(x=0, y=152)
        emp1inf = Frame(b_frame, bg="White", height=121, width=320)
        Label(emp1inf, text="Restaurant", bg="white", font="msserif 17 bold").place(
            x=72, y=0
        )
        Label(emp1inf, text="John Doe", bg="white", fg="Grey", font="msserif 10").place(
            x=72, y=37
        )
        Label(
            emp1inf, text="Phone : 999", bg="white", fg="Grey", font="msserif 10"
        ).place(x=72, y=59)
        Label(
            emp1inf,
            text="Mail : JohnDoe@google.com",
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=72, y=83)
        emp1inf.place(x=99, y=153)

        emp1f = Frame(b_frame)
        path4 = "images/roomservicenew.jpg"
        img4 = ImageTk.PhotoImage(Image.open(path4))
        emp1 = Label(emp1f, image=img4)
        emp1.image = img4
        emp1.pack()
        emp1f.place(x=657, y=152)
        emp1inf = Frame(b_frame, bg="White", height=124, width=315)
        Label(emp1inf, text="Room Service", bg="white", font="msserif 17 bold").place(
            x=55, y=0
        )
        Label(emp1inf, text="John Doe", bg="white", fg="Grey", font="msserif 10").place(
            x=55, y=37
        )
        Label(
            emp1inf, text="Phone : 999", bg="white", fg="Grey", font="msserif 10"
        ).place(x=55, y=59)
        Label(
            emp1inf,
            text="Mail : JohnDoe@google.com",
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=55, y=83)
        emp1inf.place(x=763, y=153)

        Frame(b_frame, height=13, width=250, bg="white").place(x=410, y=2)
        Frame(b_frame, height=13, width=250, bg="white").place(x=410, y=153)
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)

    # ---------------NAV MENU--------------------------------------------------
    sl_frame = Frame(root, height=130, width=1080, bg="white")
    sl_frame.place(x=0, y=70 + 6)

    path1 = "images/hotelstatus.png"
    img1 = ImageTk.PhotoImage(Image.open(path1))
    b1 = Button(
        sl_frame, image=img1, text="b2", bg="white", width=180, command=showHotel_status
    )
    b1.image = img1
    b1.place(x=50, y=0)

    path2 = "images/rooms.png"
    img2 = ImageTk.PhotoImage(Image.open(path2))
    b2 = Button(
        sl_frame, image=img2, text="b1", bg="white", width=180, command=showRooms
    )
    b2.image = img2
    b2.place(x=230, y=0)

    path3 = "images/Bookroom.png"
    img3 = ImageTk.PhotoImage(Image.open(path3))
    b3 = Button(
        sl_frame,
        image=img3,
        text="b2",
        bg="white",
        width=180,
        height=100,
        command=reserve,
    )
    b3.image = img3
    b3.place(x=410, y=0)

    path4 = "images/guests.png"
    img4 = ImageTk.PhotoImage(Image.open(path4))
    b4 = Button(
        sl_frame, image=img4, text="b2", bg="white", width=180, command=showStaff
    )
    b4.image = img4
    b4.place(x=590, y=0)

    path5 = "images/logout.png"
    img5 = ImageTk.PhotoImage(Image.open(path5))
    b5 = Button(sl_frame, image=img5, text="b2", bg="white", width=180, height=100)
    b5.image = img5
    b5.place(x=770, y=0)

    Label(sl_frame, text="Hotel Status", font="msserif 13", bg="white").place(
        x=95, y=106
    )
    Label(sl_frame, text="Rooms", font="msserif 13", bg="white").place(x=290, y=106)
    Label(sl_frame, text="Reserve", font="msserif 13", bg="white").place(x=457, y=106)
    Label(sl_frame, text="Contacts", font="msserif 13", bg="white").place(x=644, y=106)
    Label(sl_frame, text="Exit", font="msserif 13", bg="white").place(x=858, y=106)
    sl_frame.pack_propagate(False)


def call_mainroot():
    sroot.destroy()
    mainroot()


sroot.after(10, call_mainroot)
mainloop()
