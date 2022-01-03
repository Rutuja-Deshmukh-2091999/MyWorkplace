from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title("Hello Python")
root.iconbitmap('house.ico')
frame = LabelFrame(root,padx = 50,pady = 50)
frame.pack(padx = 50,pady = 50)

#r = IntVar()
#r.set("2")
def clicked(value):
    label1 = Label(frame, text=value)
    label1.update()
    label1.grid()

def popup():
    response = messagebox.askyesno("please press ok to exit","exit")
    #Label(frame,text = response).pack()
    if(response == 1):
        Label(frame,command = root.quit())


topics = [
    ("python","python"),
    ("java","java"),
    ("c++","c++"),
    ("sql","sql")
]

sub = StringVar(value="off")
sub.set(None)
#index, (key, value) in enumerate(some_dict.items())
for text,mode in topics:
    Radiobutton(frame,text = text,variable = sub,value = mode,command = lambda : clicked(sub.get())).grid(sticky = W)





#Radiobutton(frame,text = "Option 1",variable = r,value = 1,command = lambda : clicked(r.get())).grid(row = 0 ,column = 0)
#Radiobutton(frame,text = "Option 2",variable = r,value = 2,command = lambda : clicked(r.get())).grid(row = 1,column = 0)




button1 =  Button(frame,text = "This is Button",command = popup)
button1.grid(row = 5,column = 0)

root.mainloop()