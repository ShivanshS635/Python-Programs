from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x500")
root.title("WELCOME SCREEN")
root.configure(bg="cyan")

textname=StringVar()

def b1_clicked():
    root.configure(bg="red")
def b2_clicked():
    root.configure(bg="blue")
def b3_clicked():
    root.configure(bg="green")
def clickme_clicked():
    s=textname.get()
    messagebox.showinfo("Great!","Hello! "+s)
    #messagebox.showerror("Great!","Hello! "+s)
    #messagebox.showwarning("Great!","Hello! "+s)
    

L0=Label(root,text="WELCOME TO TKINTER",bg="yellow",fg="red",font=("Lucida Handwriting",30,"bold"))
L0.place(x=100,y=50)
L1=Label(root,text="Enter Your Name")
L1.place(x=100,y=250)
t1=Entry(root,width=30,textvariable=textname)
t1.place(x=200,y=250)


b1=Button(root,text="Red",width=15,command=b1_clicked)
b2=Button(root,text="Blue",width=15,command=b2_clicked)
b3=Button(root,text="Green",width=15,command=b3_clicked)
b4=Button(root,text="Click Me!",width=25,command=clickme_clicked)


b1.place(x=100,y=150)
b2.place(x=280,y=150)
b3.place(x=450,y=150)
b4.place(x=400,y=250)

root.mainloop()
