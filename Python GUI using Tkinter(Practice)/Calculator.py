from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root,width = 55,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 4,padx = 10,pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    return

def button_clear():
    e.delete(0,END)
    return

def button_add():
    f_no = e.get()
    global fnum
    global math
    math = "addition"
    fnum = int(f_no)
    e.delete(0,END)
    #s_no = e.get()
    return

def button_sub():
    f_no = e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = int(f_no)
    e.delete(0, END)
    return

def button_multi():
    f_no = e.get()
    global fnum
    global math
    math = "multiply"
    fnum = int(f_no)
    e.delete(0, END)
    return

def button_div():
    f_no = e.get()
    global fnum
    global math
    math = "divide"
    fnum = int(f_no)
    e.delete(0, END)
    return

def button_equal():
    s_no = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,fnum + int(s_no))
    if math == "subtraction":
        e.insert(0,fnum - int(s_no))
    if math == "multiply":
        e.insert(0,fnum * int(s_no))
    if math == "divide":
        e.insert(0,fnum / int(s_no))
    return



button1 = Button(root,text = "1",padx = 40,pady = 20,command =lambda: button_click(1))
button2 = Button(root,text = "2",padx = 40,pady = 20,command =lambda: button_click(2))
button3 = Button(root,text = "3",padx = 40,pady = 20,command =lambda: button_click(3))
button4 = Button(root,text = "4",padx = 40,pady = 20,command =lambda: button_click(4))
button5 = Button(root,text = "5",padx = 40,pady = 20,command =lambda: button_click(5))
button6 = Button(root,text = "6",padx = 40,pady = 20,command =lambda: button_click(6))
button7 = Button(root,text = "7",padx = 40,pady = 20,command =lambda: button_click(7))
button8 = Button(root,text = "8",padx = 40,pady = 20,command =lambda: button_click(8))
button9 = Button(root,text = "9",padx = 40,pady = 20,command =lambda: button_click(9))
button0 = Button(root,text = "0",padx = 40,pady = 20,command =lambda: button_click(0))

button_add = Button(root,text = "+",padx = 39,pady = 20,command = button_add)
button_sub = Button(root,text = "-",padx = 39,pady = 20,command = button_sub)
button_multi = Button(root,text = "*",padx = 39,pady = 20,command = button_multi)
button_div = Button(root,text = "/",padx = 39,pady = 20,command = button_div)


button_equals = Button(root,text = "=",padx = 130,pady = 20,command = button_equal)
button_clear = Button(root,text = "C",padx = 130,pady = 20,command = button_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_add.grid(row = 5,column = 0)
button_sub.grid(row = 1,column = 3)
button_multi.grid(row = 2,column = 3)
button_div.grid(row = 3,column = 3)

button_equals.grid(row = 5,column = 1,columnspan = 3)
button_clear.grid(row = 4,column = 1,columnspan = 3)



root.mainloop()