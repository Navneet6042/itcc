from tkinter import *
root=Tk()
e=Entry(root)
e.grid(row=7,column=4)
m=e.get()

def i1():
    Label(root,text="1").grid(row=6,column=6)
    
def i2():
    Label(root,text="2").grid(row=6,column=6)
    
def i3():
    Label(root,text="3").grid(row=6,column=6)
    
def i4():
    Label(root,text="4").grid(row=6,column=6)

def i5():
    Label(root,text="5").grid(row=6,column=6)

def i6():
    Label(root,text="6").grid(row=6,column=6)

def i7():
    Label(root,text="7").grid(row=6,column=6)

def i8():
    Label(root,text="8").grid(row=6,column=6)

def i9():
    Label(root,text="9").grid(row=6,column=6)

def i0():
    Label(root,text="0").grid(row=6,column=6)

l=Label(root,text=m)
l.grid(row=8,column=4)

b1=Button(root,text="1",padx=40,pady=50,command=i1)
b1.grid(row=2,column=0)

b2=Button(root,text="2",padx=40,pady=50,command=i2)
b2.grid(row=2,column=1)

b3=Button(root,text="3",padx=40,pady=50,command=i3)
b3.grid(row=2,column=2)

b4=Button(root,text="4",padx=40,pady=50,command=i4)
b4.grid(row=3,column=0)

b5=Button(root,text="5",padx=40,pady=50,command=i5)
b5.grid(row=3,column=1)

b6=Button(root,text="6",padx=40,pady=50,command=i6)
b6.grid(row=3,column=2)

b7=Button(root,text="7",padx=40,pady=50,command=i7)
b7.grid(row=4,column=0)

b8=Button(root,text="8",padx=40,pady=50,command=i8)
b8.grid(row=4,column=1)

b9=Button(root,text="9",padx=40,pady=50,command=i9)
b9.grid(row=4,column=2)

b0=Button(root,text="0",padx=40,pady=50,command=i0)
b0.grid(row=5,column=1)

bp=Button(root,text="+",padx=40,pady=50)
bp.grid(row=2,column=3)

bm=Button(root,text="X",padx=40,pady=50)
bm.grid(row=3,column=3)

bs=Button(root,text="-",padx=40,pady=50)
bs.grid(row=4,column=3)

bd=Button(root,text="/",padx=40,pady=50)
bd.grid(row=5,column=0)

be=Button(root,text="=",padx=40,pady=50)
be.grid(row=5,column=2)

bc=Button(root,text="C",padx=40,pady=50)
bc.grid(row=5,column=3)

root.mainloop()