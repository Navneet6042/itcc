from tkinter import *
r=Tk()
r.title("gst callculator")
#--------------
og=Label(r,text="original cost")
og.pack()

oge=(Entry(r))
oge.pack()


#-----------------
np=Label(r,text="net price")
np.pack()

npe=(Entry(r))
npe.pack()


#--------------

#gss=(int((npe.get()))-int((oge.get(0))))*100/int((oge.get()))
#-----------------
def btf():
    ogv=int((oge.get()))
    npv=int((npe.get()))
    l=(npv-ogv)*100/ogv
    gs=Label(r,text="GST result")
    gs.pack()

    gse=Label(r,text=l)
    gse.pack()


bb=Button(r,text="compute",command=btf)
bb.pack()


r.mainloop()
