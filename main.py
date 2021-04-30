import MySQLdb
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import re
from random import randint
import os

today = date.today()
d1 = today.strftime("%d/%m/%Y")
path = os.getcwd() + "\\bills"

x = randint(99, 400)


def create_bill(date, days, fn, ln, nop, rno):
    connection = MySQLdb.connect(
        host="localhost", database="hotel", user="root", password="pass"
    )
    cursor = connection.cursor()

    stri = "select price from Room where room_no= %d"
    args = int(rno)
    cursor.execute(stri % args)
    price = cursor.fetchone()
    p1 = int(price[0])
    p2 = p1 * int(days)
    p3 = 0.18 * p2
    p4 = p2 + p3
    global x
    refno = str(x)
    list0 = "\t\t\t\t\t\t\tReference.no :" + refno
    list1 = (
        "\n\n\t"
        + "Room Number| Customer Name | Date of Booking | Days of Stay | Total Persons |\n"
    )
    list2 = "\t-----------------------------------------------------------------------------\n"
    list3 = (
        "\t"
        + rno
        + "          |  "
        + fn
        + " "
        + ln
        + "   |    "
        + date
        + "   |     "
        + str(days)
        + "        |     "
        + str(nop)
        + "         | \n"
    )
    list5 = "\n\n\n\t\t\t   " + "Price/Night       = Rs " + str(p1) + "/-" + "\n"
    list6 = "\t\t\t   " + "Price for " + days + " days  = Rs " + str(p2) + "/-" + "\n"
    list7 = "\t\t\t   " + "GST               = Rs " + str(p3) + "/-" "\n"
    list8 = "\t\t\t   " + "GrandTotal=       = Rs " + str(p4) + "/-" + "\n"
    bill = list0 + list1 + list2 + list3 + list5 + list6 + list7 + list8
    return bill


# create_bill("11/11/1111", "1", "meet", "gajra", "1", "1")


# -----------------CONNECT DB--------------
# connection = MySQLdb.connect(
#     host="localhost", database="hotel", user="root", password="pass"
# )
# cursor = connection.cursor()

# cursor.execute(
#     "create table Room(room_no integer PRIMARY KEY, isReserved BOOLEAN DEFAULT 0, underRenovation BOOLEAN DEFAULT 0, booked_by TEXT, room_type TEXT, AC_available TEXT,  price NUMERIC, date_of_booking TEXT, days_of_stay INTEGER, no_of_customers NUMERIC)"
# )
# cursor.execute("create table Staff(role TEXT, name TEXT, phone_no TEXT, mail TEXT)")


def hotelStatus():
    connection = MySQLdb.connect(
        host="localhost", database="hotel", user="root", password="pass"
    )
    cursor = connection.cursor()
    cursor.execute("select room_no from Room")
    cursor.fetchall()
    totalRooms = cursor.rowcount

    cursor.execute("select room_no from Room where isReserved=1")
    cursor.fetchall()
    reservedRooms = cursor.rowcount

    cursor.execute("select name from Staff")
    cursor.fetchall()
    totalStaff = cursor.rowcount

    cursor.execute("select SUM(no_of_customers) from Room")
    totalCustomers = cursor.fetchone()

    cursor.execute("select room_no from Room where underRenovation=1")
    cursor.fetchall()
    renovRooms = cursor.rowcount

    availableRooms = totalRooms - reservedRooms

    return [
        totalRooms,
        reservedRooms,
        availableRooms,
        totalStaff,
        totalCustomers,
        renovRooms,
    ]


def staffStatus():
    staff = []
    connection = MySQLdb.connect(
        host="localhost", database="hotel", user="root", password="pass"
    )
    cursor = connection.cursor()
    cursor.execute("select * from Staff")
    row = cursor.fetchone()
    while row is not None:
        staff.append(row)
        row = cursor.fetchone()
    return staff


def roomStatus(roomNum):
    connection = MySQLdb.connect(
        host="localhost", database="hotel", user="root", password="pass"
    )
    cursor = connection.cursor()

    stri = "select * from Room where room_no= %d"
    args = roomNum
    cursor.execute(stri % args)
    room = cursor.fetchone()
    return room


def addRoom(rno, underRen, roomType, ac, price):

    connection = MySQLdb.connect(
        host="localhost", database="hotel", user="root", password="pass"
    )
    cursor = connection.cursor()

    stri = "insert into Room(room_no, underRenovation, room_type, AC_available, price) values('%d', '%d', '%s', '%s', '%d')"
    args = (rno, underRen, roomType, ac, price)
    try:
        cursor.execute(stri % args)
        connection.commit()
        messagebox.showinfo("success", "Room successfully added!")

    except (Exception) as error:
        print("Error while using MySQL table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def addStaff(role, name, phone, email):

    connection = MySQLdb.connect(
        host="localhost", database="hotel", user="root", password="pass"
    )
    cursor = connection.cursor()

    stri = (
        "insert into Staff(role, name, phone_no, mail) values('%s', '%s', '%s', '%s')"
    )
    args = (role, name, phone, email)
    try:
        cursor.execute(stri % args)
        connection.commit()
        print("Staff added")

    except (Exception) as error:
        print("Error while using MySQL table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


# addRoom(1, 0, "Deluxe", "Yes", 4500)
# addRoom(2, 0, "Deluxe", "No", 4500)
# addRoom(3, 1, "Standard", "Yes", 3500)
# addRoom(4, 1, "Standard", "No", 2500)
# addRoom(5, 0, "Suite", "Yes", 6500)
# addRoom(6, 1, "Standard", "Yes", 3500)
# addRoom(7, 0, "Suite", "Yes", 6500)
# addRoom(8, 0, "Deluxe", "No", 4500)
# addRoom(9, 0, "Deluxe", "Yes", 5500)
# addRoom(10, 0, "Deluxe", "No", 4500)
# addStaff("Receptionist", "Pooja Verma", "9383555686", "Poojaverma@google.com")
# addStaff("Restaurant", "Gordon Ramsey", "9323252566", "gordonramsey@google.com")
# addStaff("Room Service", "Maya Bhatt", "8453256577", "mayabhatt@google.com")
# addStaff("Manager", "Vijay Nath", "9457283456", "vijaynath@gmail.com")
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


def mainroot():
    root = Tk()
    root.geometry("1080x500")
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg="white")
    root.title("Hotel Management System")
    top_frame = Frame(root, height=70, width=1080, bg="red4")
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

        lst = hotelStatus()

        tor = lst[0]
        rer = lst[1]
        avr = lst[2]
        tos = lst[3]
        toc = lst[4]
        renRooms = lst[5]

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
        Label(smf4, text=toc, fg="red4", bg="white", font="msserif 50").pack(
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
        Label(smf6, text=renRooms, fg="red4", bg="white", font="msserif 50").place(
            x=60, y=60
        )

        redf1 = Frame(b_frame, height=8, width=1080, bg="dark orange")

        redf1.place(x=0, y=22)
        Label(
            b_frame, text="Hotel Status", font="msserif 12", bg="red4", fg="white"
        ).pack(anchor="center")
        redf1.pack_propagate(False)

    def showRooms():

        connection = MySQLdb.connect(
            host="localhost",
            database="hotel",
            user="root",
            password="pass",
        )
        cursor = connection.cursor()
        cursor.execute("select room_no from Room")
        cursor.fetchall()
        tor = cursor.rowcount

        b_frame = Frame(root, height=400, width=1080, bg="gray91")
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        path = "images/texture_bg.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        sidebuttons = Text(b_frame, width=1, height=19)
        sc = Scrollbar(
            b_frame, command=sidebuttons.yview, width=10, bg="lightsteelblue3"
        )
        sidebuttons.configure(yscrollcommand=sc.set)
        sc.pack(side="left", fill=Y)
        sidebuttons.place(x=10, y=0)

        def roomdet(rno):

            room = roomStatus(rno)
            if room[1]:
                reserved = "Yes"
                bookedBy = room[3]
                date = room[7]
                days = room[8]
                cust = room[9]
            else:
                reserved = "No"
                bookedBy = "-"
                date = "-"
                days = "-"
                cust = "-"

            if room[2]:
                renov = "Yes"
            else:
                renov = "No"

            rtype = room[4]

            ac = room[5]

            price = room[6]

            Label(
                b_frame,
                text="Room %s" % rno,
                font="msserif 15",
                fg="white",
                bg="red4",
                width=10,
            ).place(x=535, y=0)

            smf1 = Frame(b_frame, height=120, width=145, bg="white")
            hline = Frame(b_frame, height=10, width=960, bg="orange")
            hline.place(x=122, y=27)
            vline = Frame(b_frame, height=400, width=7, bg="lightsteelblue3")
            vline.place(x=122, y=0)

            tr = Label(
                smf1,
                text="Room Type:",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack()
            smf1.pack_propagate(False)
            smf1.place(x=129 + 18, y=50)
            Label(smf1, text=rtype, fg="red4", bg="white", font="msserif 22").pack()

            smf2 = Frame(b_frame, height=120, width=145, bg="white")
            tr = Label(
                smf2,
                text="AC Available?",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 2 + 5 + 3 * 2 + 20, y=50)
            Label(smf2, text=ac, fg="red4", bg="white", font="msserif 18").pack()

            smf2 = Frame(b_frame, height=120, width=175, bg="white")
            tr = Label(
                smf2,
                text="Under Renovation?",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 3 + 12 + 5 * 2 + 3 * 3 + 20, y=50)
            Label(smf2, text=renov, fg="red4", bg="white", font="msserif 18").pack()
            smf2 = Frame(b_frame, height=120, width=145, bg="white")
            tr = Label(
                smf2,
                text="Price",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 4 + 12 * 2 + 5 * 3 + 3 * 4 + 50, y=50)
            Label(smf2, text=price, fg="red4", bg="white", font="msserif 18").pack()
            smf2 = Frame(b_frame, height=120, width=145, bg="white")
            tr = Label(
                smf2,
                text=" Reserved?",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 5 + 12 * 3 + 5 * 4 + 3 * 5 + 50, y=50)
            Label(smf2, text=reserved, fg="red4", bg="white", font="msserif 18").pack()

            smf1 = Frame(b_frame, height=120, width=175, bg="white")
            tr = Label(
                smf1,
                text="Booked By:",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack()
            smf1.pack_propagate(False)
            smf1.place(x=129 + 18, y=190)
            Label(smf1, text=bookedBy, fg="red4", bg="white", font="msserif 18").pack()

            smf2 = Frame(b_frame, height=120, width=175, bg="white")
            tr = Label(
                smf2,
                text="Date of booking",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 2 + 5 + 3 * 2 + 50, y=190)
            Label(smf2, text=date, fg="red4", bg="white", font="msserif 18").pack()

            smf2 = Frame(b_frame, height=120, width=175, bg="white")
            tr = Label(
                smf2,
                text="Days of stay",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 3 + 12 + 5 * 2 + 3 * 3 + 80, y=190)
            Label(smf2, text=days, fg="red4", bg="white", font="msserif 18").pack()
            smf2 = Frame(b_frame, height=120, width=145, bg="white")
            tr = Label(
                smf2,
                text="Total Persons",
                fg="white",
                bg="red4",
                width=100,
                height=2,
                font="msserif 15",
            )
            tr.pack(side="top")
            smf2.pack_propagate(False)
            smf2.place(x=140 * 4 + 12 * 2 + 5 * 3 + 3 * 4 + 110, y=190)
            Label(smf2, text=cust, fg="red4", bg="white", font="msserif 18").pack()

        button = list()
        for i in range(tor):
            button.append(
                Button(
                    b_frame,
                    font="mssherif 10",
                    text="Room " + str(i + 1),
                    bg="white",
                    fg="red4",
                    width=10,
                    command=lambda x=i: roomdet(x + 1),
                )
            )
            sidebuttons.window_create("end", window=button[i])
            sidebuttons.insert("end", "\n")
        add = Button(
            b_frame,
            text="Add Room",
            bg="white",
            fg="red4",
            font="timenewroman 11",
            command=add_room,
        )
        add.place(x=900, y=225)
        roomdet(1)

    def add_room():
        b_frame = Frame(root, height=400, width=1080, bg="gray91")
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        path = "images/texture_bg.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        Label(
            b_frame, text="Add Room", bg="gray93", fg="red4", font="Timesnewroman 20"
        ).place(x=480, y=20)
        rnf = Frame(b_frame, height=1, width=1)
        rno = Entry(rnf)

        pnf = Frame(b_frame, height=1, width=1)
        pr = Entry(pnf)

        rno.insert(0, "Room no. *")
        pr.insert(0, "Room Price *")

        def on_entry_click1(event):
            if rno.get() == "Room no. *":
                rno.delete(0, END)
                rno.insert(0, "")

        def on_entry_click3(event):
            if pr.get() == "Room Price *":
                pr.delete(0, END)
                pr.insert(0, "")

        def on_exit1(event):
            if rno.get() == "":
                rno.insert(0, "Room no. *")

        def on_exit3(event):
            if pr.get() == "":
                pr.insert(0, "Room Price *")

        rno.bind("<FocusIn>", on_entry_click1)
        pr.bind("<FocusIn>", on_entry_click3)
        rno.bind("<FocusOut>", on_exit1)
        pr.bind("<FocusOut>", on_exit3)

        rno.pack(ipady=4, ipadx=15)
        pr.pack(ipady=4, ipadx=15)
        rnf.place(x=470, y=72)
        pnf.place(x=470, y=112)

        style = ttk.Style()
        style.map("TCombobox", fieldbackground=[("readonly", "white")])
        Label(b_frame, text="Room Typ.:", bg="gray93", font="17").place(x=360, y=152)
        nb = ttk.Combobox(
            b_frame,
            values=["please select...", "standard", "deluxe", "suite"],
            state="readonly",
            width=22,
        )
        nb.place(x=470, y=152)
        nb.current(0)

        Label(b_frame, text="AC :", font="17", bg="gray93").place(x=422, y=192)
        acf = ttk.Combobox(
            b_frame,
            values=["please select...", "Yes", "No"],
            state="readonly",
            width=22,
        )
        acf.place(x=470, y=192)
        acf.current(0)
        add = Button(
            b_frame,
            text="Add it!",
            bg="white",
            fg="red4",
            font="timenewroman 11",
            command=lambda: addRoom(
                int(rno.get()), 0, nb.get(), acf.get(), int(pr.get())
            ),
        )
        add.place(x=470, y=232)

    def reserve():
        b_frame = Frame(root, height=420, width=1080, bg="gray89")
        path = "images/texture_bg.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=420, width=1080)
        label.image = img
        label.place(x=0, y=0)

        vline = Frame(b_frame, height=400, width=7, bg="lightsteelblue3")
        vline.place(x=700, y=0)

        Label(
            b_frame, text="Personal Information", font="msserif 15", bg="gray93"
        ).place(x=225, y=0)

        fnf = Frame(b_frame, height=1, width=1)
        fn = Entry(fnf)

        lnf = Frame(b_frame, height=1, width=1)
        ln = Entry(lnf)

        fn.insert(0, "First Name *")
        ln.insert(0, "Last Name *")

        def on_entry_click1(event):
            if fn.get() == "First Name *":
                fn.delete(0, END)
                fn.insert(0, "")

        def on_entry_click3(event):
            if ln.get() == "Last Name *":
                ln.delete(0, END)
                ln.insert(0, "")

        def on_exit1(event):
            if fn.get() == "":
                fn.insert(0, "First Name *")

        def on_exit3(event):
            if ln.get() == "":
                ln.insert(0, "Last Name *")

        fn.bind("<FocusIn>", on_entry_click1)
        ln.bind("<FocusIn>", on_entry_click3)
        fn.bind("<FocusOut>", on_exit1)
        ln.bind("<FocusOut>", on_exit3)

        fn.pack(ipady=4, ipadx=15)
        ln.pack(ipady=4, ipadx=15)
        fnf.place(x=20, y=42)
        lnf.place(x=235, y=42)

        Label(
            b_frame, text="Contact Information", font="msserif 15", bg="gray93"
        ).place(x=225, y=90)

        cnf = Frame(b_frame, height=1, width=1)
        cn = Entry(cnf)

        emf = Frame(b_frame, height=1, width=1)
        em = Entry(emf)

        cn.insert(0, "Contact Number *")
        em.insert(0, "Email *")

        def on_entry_click4(event):
            if cn.get() == "Contact Number *":
                cn.delete(0, END)
                cn.insert(0, "")

        def on_entry_click5(event):
            if em.get() == "Email *":
                em.delete(0, END)
                em.insert(0, "")

        def on_exit4(event):
            if cn.get() == "":
                cn.insert(0, "Contact Number *")

        def on_exit5(event):
            if em.get() == "":
                em.insert(0, "Email *")

        cn.bind("<FocusIn>", on_entry_click4)
        em.bind("<FocusIn>", on_entry_click5)

        cn.bind("<FocusOut>", on_exit4)
        em.bind("<FocusOut>", on_exit5)

        cn.pack(ipady=4, ipadx=15)
        em.pack(ipady=4, ipadx=15)
        cnf.place(x=20, y=130)
        emf.place(x=235, y=130)

        Label(
            b_frame, text="Reservation Information", font="msserif 15", bg="gray93"
        ).place(x=210, y=175)

        nopf = Frame(b_frame, height=1, width=1)
        nop = Entry(nopf)

        nodf = Frame(b_frame, height=1, width=1)
        nod = Entry(nodf)

        nop.insert(0, "Number of Persons *")
        nod.insert(0, "Number of Days of Stay *")

        def on_entry_click7(event):
            if nop.get() == "Number of Persons *":
                nop.delete(0, END)
                nop.insert(0, "")

        def on_entry_click8(event):
            if nod.get() == "Number of Days of Stay *":
                nod.delete(0, END)
                nod.insert(0, "")

        def on_exit7(event):
            if nop.get() == "":
                nop.insert(0, "Number of Persons *")

        def on_exit8(event):
            if nod.get() == "":
                nod.insert(0, "Number of Days of Stay *")

        nop.bind("<FocusIn>", on_entry_click7)
        nod.bind("<FocusIn>", on_entry_click8)
        nop.bind("<FocusOut>", on_exit7)
        nod.bind("<FocusOut>", on_exit8)

        nop.pack(ipady=4, ipadx=15)
        nod.pack(ipady=4, ipadx=15)
        nopf.place(x=20, y=220)
        nodf.place(x=235, y=220)

        roomnf = Frame(b_frame, height=1, width=1)
        roomn = Entry(roomnf)
        roomn.insert(0, "Enter Room Number *")

        def on_entry_click10(event):
            if roomn.get() == "Enter Room Number *":
                roomn.delete(0, END)
                roomn.insert(0, "")

        def on_exit10(event):
            if roomn.get() == "":
                roomn.insert(0, "Enter Room Number *")

        roomn.bind("<FocusIn>", on_entry_click10)
        roomn.bind("<FocusOut>", on_exit10)
        roomn.pack(ipady=4, ipadx=15)
        roomnf.place(x=20, y=270)

        # -------------------------------------------------------filters-------------------------

        Label(b_frame, text="Filter", font="msserif 20", bg="gray93").place(x=850, y=0)

        style = ttk.Style()
        style.map("TCombobox", fieldbackground=[("readonly", "white")])
        Label(b_frame, text="Room Typ.:", bg="gray93", font="17").place(x=730, y=50)
        nb = ttk.Combobox(
            b_frame,
            values=["please select...", "standard", "deluxe", "suite"],
            state="readonly",
            width=22,
        )
        nb.place(x=840, y=50)
        nb.current(0)

        Label(b_frame, text="AC :", font="17", bg="gray93").place(x=792, y=75)
        acf = ttk.Combobox(
            b_frame,
            values=["please select...", "Yes", "No"],
            state="readonly",
            width=22,
        )
        acf.place(x=840, y=75)
        acf.current(0)

        listofrooms = Listbox(b_frame, height=6, width=39)
        listofrooms.place(x=775, y=190)
        listofrooms.insert(END, "Rooms of Your Choice will appear Here")
        listofrooms.insert(END, "once you apply filter")

        def findrooms():
            connection = MySQLdb.connect(
                host="localhost",
                database="hotel",
                user="root",
                password="pass",
            )
            cursor = connection.cursor()
            stri = "select room_no,price,isReserved from Room where room_type=%s and AC_available=%s order by price asc"
            args = (nb.get(), acf.get())

            cursor.execute(stri, args)
            x = cursor.fetchall()
            print(x)
            listofrooms.delete(0, END)
            if len(x) == 0:
                listofrooms.insert(END, "No Rooms Found!")
            else:
                for i in x:
                    if i[2]:
                        b = "Yes"
                    else:
                        b = "No"
                    listofrooms.insert(
                        END,
                        "Room No. -"
                        + str(i[0])
                        + " - Price - "
                        + str(i[1])
                        + " - booked - "
                        + b,
                    )

        findrooms = Button(
            b_frame,
            text="Find Rooms",
            bg="white",
            fg="cyan4",
            font="timenewroman 9",
            activebackground="green",
            command=findrooms,
        )
        findrooms.place(x=850, y=155)

        scrollbar = Scrollbar(b_frame, orient="vertical")
        scrollbar.config(command=listofrooms.yview)
        scrollbar.place(x=1014, y=191, height=111)
        listofrooms.config(yscrollcommand=scrollbar.set)

        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()

        def booking():
            regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
            if (
                fn.get() == "First Name"
                or ln.get() == "Last Name"
                or cn.get() == "Contact Number *"
                or em.get() == "Email"
                or nop.get() == "Number of Persons *"
                or nod.get() == "Number of Days of Stay *"
                or roomn.get() == "Enter Room Number *"
            ):
                messagebox.showinfo("Incomplete", "Fill All the Fields marked by *")

            # 1) Begins with 6 or 7 or 8 or 9. Then contains 9 digits
            elif re.search(r"^[6-9]\d{9}$", cn.get()) == None:
                messagebox.showinfo("Incomplete", "Enter valid mobile number!")

            elif re.search(regex, em.get()) == None:
                messagebox.showinfo("Incomplete", "Enter valid Email ID!")
            else:
                connection = MySQLdb.connect(
                    host="localhost",
                    database="hotel",
                    user="root",
                    password="pass",
                )
                cursor = connection.cursor()
                stri = "select isReserved,underRenovation from Room where room_no = %d"
                args = int(roomn.get())
                cursor.execute(stri % args)
                temp = cursor.fetchone()
                if temp == None:
                    messagebox.showwarning(
                        "ERROR",
                        "Room number " + roomn.get() + " doesnt exist",
                    )
                elif temp[0] == 1:
                    messagebox.showwarning(
                        "Room is Reserved",
                        "Room number " + roomn.get() + " is Reserved",
                    )

                elif temp[1] == 1:
                    messagebox.showwarning(
                        "Room is under renovation!",
                        "Room number " + roomn.get() + " is under renovation",
                    )
                else:
                    connection = MySQLdb.connect(
                        host="localhost",
                        database="hotel",
                        user="root",
                        password="pass",
                    )
                    cursor = connection.cursor()
                    stri = "update Room set isReserved=1,date_of_booking='%s',days_of_stay=%d,booked_by='%s',no_of_customers=%d where room_no=%d"
                    args = (
                        d1,
                        int(nod.get()),
                        fn.get() + " " + ln.get(),
                        int(nop.get()),
                        int(roomn.get()),
                    )
                    try:
                        cursor.execute(stri % args)
                        connection.commit()
                    except (Exception) as error:
                        print("Error while using MySQL table", error)
                    finally:
                        if connection:
                            cursor.close()
                            connection.close()

                    messagebox.showinfo("Successful", "Room Booked successfully")
                    ask = messagebox.askyesno(
                        "Successful",
                        "Room booked successfully.\nDo you want to print reciept ?",
                    )
                    if ask:
                        global x
                        refno = str(x)
                        title = refno + ".txt"
                        global path
                        with open(os.path.join(path, title), "w") as file1:
                            toFile = create_bill(
                                d1,
                                nod.get(),
                                fn.get(),
                                ln.get(),
                                nop.get(),
                                roomn.get(),
                            )
                            file1.write(toFile)
                        messagebox.showinfo("Information", "Bill Generated")
                        x = randint(99, 400)

                    fn.delete(0, END)
                    ln.delete(0, END)
                    cn.delete(0, END)
                    em.delete(0, END)
                    nop.delete(0, END)
                    nod.delete(0, END)
                    roomn.delete(0, END)

                    fn.insert(0, "First Name *")
                    ln.insert(0, "Last Name *")
                    cn.insert(0, "Contact Number *")
                    em.insert(0, "Email *")
                    nop.insert(0, "Number of Persons *")
                    nod.insert(0, "Number of Days of Stay *")
                    roomn.insert(0, "Enter Room Number *")

        def unreserve():
            if roomn.get() == "Enter Room Number *" or "":
                messagebox.showinfo("Incomplete", "Please enter room number")
            else:
                connection = MySQLdb.connect(
                    host="localhost",
                    database="hotel",
                    user="root",
                    password="pass",
                )
                cursor = connection.cursor()
                stri = "update Room set isReserved=0,date_of_booking=NULL,days_of_stay=NULL,booked_by=NULL,no_of_customers=NULL where room_no=%d"
                args = int(roomn.get())
                try:
                    cursor.execute(stri % args)
                    connection.commit()
                except (Exception) as error:
                    print("Error while using MySQL table", error)
                finally:
                    if connection:
                        cursor.close()
                        connection.close()
                messagebox.showinfo("Successful", "Room unreserved!")
                roomn.delete(0, END)
                roomn.insert(0, "Enter Room Number *")

        Res = Button(
            b_frame,
            text="Reserve",
            bg="white",
            fg="red4",
            font="timenewroman 11",
            command=booking,
        )
        Res.place(x=235, y=270)

        unres = Button(
            b_frame,
            text="Unreserve",
            bg="white",
            fg="red4",
            font="timenewroman 11",
            command=unreserve,
        )
        unres.place(x=327, y=270)

        scrollbar = Scrollbar(b_frame, orient="vertical")
        scrollbar.config(command=listofrooms.yview)
        scrollbar.place(x=1014, y=191, height=111)
        listofrooms.config(yscrollcommand=scrollbar.set)

        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()

    def exit():
        q = messagebox.askyesno("Exit", "Do you really want to exit ?")
        if q:
            root.destroy()

    def showStaff():

        staff = staffStatus()
        employ1 = staff[0]
        employ2 = staff[1]
        employ3 = staff[2]
        employ4 = staff[3]

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
        Label(emp1inf, text=employ1[0], bg="white", font="msserif 17 bold").place(
            x=60, y=0
        )
        Label(emp1inf, text=employ1[1], bg="white", fg="Grey", font="msserif 10").place(
            x=60, y=37
        )
        Label(
            emp1inf,
            text="Phone : " + employ1[2],
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=60, y=59)
        Label(
            emp1inf,
            text="Mail : " + employ1[3],
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
        Label(emp1inf, text=employ2[0], bg="white", font="msserif 17 bold").place(
            x=45, y=0
        )
        Label(emp1inf, text=employ2[1], bg="white", fg="Grey", font="msserif 10").place(
            x=45, y=37
        )
        Label(
            emp1inf,
            text="Phone : " + employ2[2],
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=45, y=59)
        Label(
            emp1inf,
            text="Mail : " + employ2[3],
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
        Label(emp1inf, text=employ3[0], bg="white", font="msserif 17 bold").place(
            x=72, y=0
        )
        Label(emp1inf, text=employ3[1], bg="white", fg="Grey", font="msserif 10").place(
            x=72, y=37
        )
        Label(
            emp1inf,
            text="Phone : " + employ3[2],
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=72, y=59)
        Label(
            emp1inf,
            text="Mail : " + employ3[3],
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
        Label(emp1inf, text=employ4[0], bg="white", font="msserif 17 bold").place(
            x=55, y=0
        )
        Label(emp1inf, text=employ4[1], bg="white", fg="Grey", font="msserif 10").place(
            x=55, y=37
        )
        Label(
            emp1inf,
            text="Phone : " + employ4[2],
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=55, y=59)
        Label(
            emp1inf,
            text="Mail : " + employ4[3],
            bg="white",
            fg="Grey",
            font="msserif 10",
        ).place(x=55, y=83)
        emp1inf.place(x=763, y=153)

        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)

    # ---------------NAV MENU--------------------------------------------------
    sl_frame = Frame(root, height=130, width=1080, bg="white")
    sl_frame.place(x=32.5, y=70 + 6)

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
    b5 = Button(
        sl_frame, image=img5, text="b2", bg="white", width=180, height=100, command=exit
    )
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

    redf = Frame(root, height=6, width=1080, bg="lightsteelblue3")
    redf.place(x=0, y=70)
    redf1 = Frame(root, height=40, width=1080, bg="lightsteelblue3")
    redf1.place(x=0, y=210)

    reserve()
    mainloop()


def call_mainroot():
    sroot.destroy()
    mainroot()


sroot.after(3000, call_mainroot)
mainloop()
