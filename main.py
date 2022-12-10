from tkinter import *


def plus():
    a = int(number1.get())
    b = int(number2.get())
    c = a+b
    lab['text'] = str(c)

def minus():
    a = int(number1.get())
    b = int(number2.get())
    c = a-b
    lab['text'] = str(c)

def um():
    a = int(number1.get())
    b = int(number2.get())
    c = a*b
    lab['text'] = str(c)

def de():
    a = int(number1.get())
    b = int(number2.get())
    if b == 0:
        lab['text'] = "Ошибка. На 0 делить нельзя"
    else:
        c = a/b
        lab['text'] = str(c)

def st():
    a = int(number1.get())
    b = int(number2.get())
    c = a**b
    lab['text'] = str(c)

root = Tk()

number1 = Entry(width=20, background="light blue", foreground="dark slate gray")
number2 = Entry(width=20, background="light blue", foreground="dark slate gray")
lab = Label(background='light blue', foreground='dark slate gray', border="2")
p = Button(width=15,text='+',command=plus, border="10", background="dark slate gray")
m = Button(width=15,text='-',command=minus, border="10", background="dark slate gray")
u = Button(width=15,text='*',command=um, border="10", background="dark slate gray")
d = Button(width=15,text='/',command=de, border="10", background="dark slate gray")
s = Button(width=15,text='x^y',command=st, border="10", background="dark slate gray")



number1.pack(fill=X)
number2.pack(fill=X)
lab.pack(fill=X)
p.pack()
m.pack()
u.pack()
d.pack()
s.pack()

root.mainloop()
