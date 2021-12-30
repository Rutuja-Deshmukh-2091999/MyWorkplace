from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Hello Python")
root.iconbitmap('house.ico')

img0 = ImageTk.PhotoImage(Image.open("images/pythonimage.jpg"))
img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))


img_list = [img0,img1,img2,img3]

status = Label(root,text = "Image 1 of" + str(len(img_list)),bd = 1, relief = SUNKEN,anchor = E)

label1 = Label(image = img0)
label1.grid(row = 0,column = 0,columnspan = 3)

def forward(image_no):
    global label1
    global button_back
    global button_forward

    label1.grid_forget()
    label1 = Label(image = img_list[image_no-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_no+1))
    button_back = Button(root, text="<<", command=lambda:back(image_no-1))
    if image_no == 4:
        button_forward = Button(root,text = ">>",state = DISABLED)
    label1.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root,text = "Image "+str(image_no)+ " of" + str(len(img_list)),bd = 1, relief = SUNKEN,anchor = E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    return

def back(image_no):
    global label1
    global button_back
    global button_forward

    label1.grid_forget()
    label1 = Label(image=img_list[image_no - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_no + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_no - 1))
    if image_no == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    label1.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image " + str(image_no) + " of" + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    return

button_back = Button(root,text = "<<",command = back,state = DISABLED)
button_exit = Button(root,text = "Exit",command = root.quit)
button_forward = Button(root,text = ">>",command =lambda:forward(2))

status.grid(row = 2,column = 0,columnspan = 3,sticky = W+E)
button_back.grid(row = 1,column = 0)
button_exit.grid(row = 1,column = 1)
button_forward.grid(row = 1,column = 2,pady = 20)
root.mainloop()
