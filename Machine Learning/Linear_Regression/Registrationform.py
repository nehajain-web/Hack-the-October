import sqlite3 as s
con=s.connect("F:/sms2.db")
c=con.cursor()
c.execute("create table if not exists student(name char(30),mob int,email char(30))")


from tkinter import *
import tkinter.messagebox as m
w=Tk()
v1=StringVar()
v2=StringVar()
v3=StringVar()
def submit():
    name=v1.get()
    mob=int(v2.get())
    email=v3.get()
    c.execute("insert into student values('%s',%d,'%s')"%(name,mob,email))
    con.commit()
    m.showinfo(title="submit",message="record submitted successfully")
    
def reset():
    pass
L1=Label(w,text="Name",font=("arial",20,"bold"))
L2=Label(w,text="Mob",font=("arial",20,"bold"))
L3=Label(w,text="Email",font=("arial",20,"bold"))
E1=Entry(w,font=("arial",20,"bold"),textvariable=v1)
E2=Entry(w,font=("arial",20,"bold"),textvariable=v2)
E3=Entry(w,font=("arial",20,"bold"),textvariable=v3)
B1=Button(w,text="Submit",font=("arial",20,"bold"),command=submit)
B2=Button(w,text="Reset",font=("arial",20,"bold"),command=reset)
L1.grid(row=1,column=1)
L2.grid(row=2,column=1)
L3.grid(row=3,column=1)
E1.grid(row=1,column=2)
E2.grid(row=2,column=2)
E3.grid(row=3,column=2)
B1.grid(row=4,column=1)
B2.grid(row=4,column=2)
w.mainloop()
