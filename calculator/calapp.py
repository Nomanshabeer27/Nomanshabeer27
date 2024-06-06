# library neccessry
import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = "+"


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)


def btn_div_clicked():
    global A     # global statement
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn_mutl_clicked():
    global A     # global statement
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)


def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)


def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_zero_isclicked():
    global val
    val = val + "0"
    data.set(val)


def btn_minu_clicked():
    global A     # global statement
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


# This function use to clear button pressed then all data clear  which we


def c_pressed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def btn_plus_clicked():
    global A     # global statement
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


# work to operator fuction using with condition if elif or else
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        C = A / x
        data.set(C)
        val = str(C)
        if x == 0:
            messagebox.showerror("error", "division is not 0 supported ")
            val = ""
            A = ""
            data.set(val)
        else:
            x = int(A / x)
            data.set(C)
            val = str(C)


root = tkinter.Tk()
root.geometry("300x350+300+300")

root.resizable(0, 0)
root.title("calculator")
# diclare one varibal     work variable for label variable
data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,  # check the location
    font=("Avolon", 20),
    textvariable=data,
    fg="#000000",
    background="#ffffff"  # work bg colour change

)
lbl.pack(expand=True, fill="both")
btnrow1 = Frame(root, bg="#000000")

btnrow1.pack(expand=True, fill="both",)

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")


btn1 = Button(
    btnrow1,
    text="1",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,

)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,

)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both")
btndivision = Button(
    btnrow1,
    text="/",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked,

)
btndivision.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text="4",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked



)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,

)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,

)
btn6.pack(side=LEFT, expand=True, fill="both")
btnmutl = Button(
    btnrow2,
    text="*",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_mutl_clicked,

)
btnmutl.pack(side=LEFT, expand=True, fill="both")


btn7 = Button(
    btnrow3,
    text="7",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,

)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,

)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,

)
btn9.pack(side=LEFT, expand=True, fill="both")
btnminu = Button(
    btnrow3,
    text="-",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_minu_clicked,

)
btnminu.pack(side=LEFT, expand=True, fill="both")


btnclear = Button(
    btnrow4,
    text="C",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=c_pressed,

)
btnclear.pack(side=LEFT, expand=True, fill="both")

btnzero = Button(
    btnrow4,
    text="0",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_zero_isclicked,

)
btnzero.pack(side=LEFT, expand=True, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=result,

)
btnequal.pack(side=LEFT, expand=True, fill="both")
btnplus = Button(
    btnrow4,
    text="+",
    font=("Avolon", 22),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked,


)
btnplus.pack(side=LEFT, expand=True, fill="both")


root.mainloop()
