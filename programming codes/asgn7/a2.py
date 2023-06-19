from tkinter import *
import calendar as c 

r=Tk()
r.title("calender")
g=Entry(r,text="enter year")
g.pack()

def pp():
    yr=int(g.get())
    p=Label(r,text=(c.calendar(yr)))
    p.pack()
    
b=Button(r,text="entre year for calendar",command=pp)
b.pack()
r.mainloop()