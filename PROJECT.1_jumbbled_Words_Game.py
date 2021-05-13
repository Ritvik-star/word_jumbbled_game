import tkinter
from tkinter import *
from tkinter import font
import random
from tkinter import messagebox


root = tkinter.Tk()
root.geometry("400x500")
root.configure(background="#000000")

answer = ["java",
    "python",
    "ruby",
    "kotlin",
    "cpp",
    "erlang",
    "swift",
    "php",
    "sql",
    "mysql",
    "mongodb",
    "nodejs",
    "expressjs",
    "jquery"]

words = [
    "avaj",
    "thonpy",
    "ybru",
    "linkot",
    "pcp",
    "langer",
    "tfswi",
    "hpp",
    "lqs",
    "lqsym",
    "dbmonog",
    "sjonde",
    "sjexpress",
    "queryj"
]

num = random.randrange(0,14,1)

def defualt():
    global words,answer,num
    lbl.config(text = words[num])

def checkans():
    global words,answer,num
    var = e1.get()
    if var == answer[num]:
        messagebox.showinfo("success","This is correct")
        reset()
    else:
        messagebox.showerror("fail","This is incorrect")
        e1.delete(0, END)    


def reset():
    global words,answer,num
    num = random.randrange(0,14,1)
    lbl.config(text = words[num])
    e1.delete(0,END)


lbl = Label(
    root,
    text= "your text here",
    font = ("Times New Roman",18),
    background="#000000",
    foreground="#ffffff",
    
)
lbl.pack(pady=30)


ans1 = StringVar()

e1 = Entry(
    root,
    font = ("Times New Roman",16),
    textvariable= ans1
)
e1.pack(ipadx=5,ipady=5)

btncheck = Button(
    root,
    text="Check",
    font = ("Times New Roman",16),
    bg="#564a4a",
    fg="#907fa4",
    relief="groove",
    command= checkans,
)
btncheck.pack(pady=30)

btnreset = Button(
    root,
    text="Reset",
    font = ("Times New Roman",16),
    bg="#564a4a",
    fg="#907fa4",
    relief="groove",
    command= reset,
)
btnreset.pack()

defualt()

root.mainloop()