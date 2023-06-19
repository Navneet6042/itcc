from tkinter import *
r=Tk()
r.title("calculator")
ee=Entry(r)
ee.grid(row=0,column=0,columnspan=4, padx=5, pady=5)
#btn creation
m7=Button(r,text=7)
m7.grid(row=0,column=0,padx=5,pady=5)

m8=Button(r,text=8)
m8.grid(row=0,column=1,padx=5,pady=5)

m9=Button(r,text=9)
m9.grid(row=0,column=2,padx=5,pady=5)

m4=Button(r,text=4)
m4.grid(row=1,column=0,padx=5,pady=5)

m5=Button(r,text=5)
m5.grid(row=1,column=1,padx=5,pady=5)

m6=Button(r,text=6)
m6.grid(row=1,column=2,padx=5,pady=5)

m1=Button(r,text=1)
m1.grid(row=2,column=0,padx=5,pady=5)

m2=Button(r,text=2)
m2.grid(row=2,column=1,padx=5,pady=5)

m3=Button(r,text=3)
m3.grid(row=2,column=2,padx=5,pady=5)

m0=Button(r,text=0)
m0.grid(row=3,column=1,padx=5,pady=5)

mx=Button(r,text="+")
mx.grid(row=3,column=0,padx=5,pady=5)

mm=Button(r,text="-")
mx.grid(row=3,column=2,padx=5,pady=5)

mX=Button(r,text="X")
mx.grid(row=0,column=3,padx=5,pady=5)

md=Button(r,text="/")
mx.grid(row=1,column=3,padx=5,pady=5)

r.mainloop()