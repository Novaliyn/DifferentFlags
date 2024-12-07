from tkinter import *
import random

#Convert button clicks into variables.
def button_click(id):
    global flag
    flag = int(id)
    if flag == 0:
        flag = random.randint(1,X)
    update()

#Clears canvas.
def update():
    for widget in root.winfo_children():
        widget.destroy()

#created the flag and shapes.
    if flag == 1:
        #North Macedonia
        screen = Canvas(root, width=400, height=300, bg="red")
        screen.create_polygon(0,0,200,150,80,0,0,0, fill="yellow")
        screen.create_polygon(175,0,200,150,225,0,175,0, fill="yellow")
        screen.create_polygon(400,0,200,150,320,0,400,0, fill="yellow")
        screen.create_polygon(0,125,200,150,0,175,0,125, fill="yellow")
        screen.create_polygon(0,300,200,150,80,300,0,300, fill="yellow")
        screen.create_polygon(175,300,200,150,225,300,175,300, fill="yellow")
        screen.create_polygon(400,300,200,150,320,300,400,300, fill="yellow")
        screen.create_polygon(400,125,200,150,400,175,400,175, fill="yellow")
        screen.create_oval(170,120,230,180, fill="yellow", outline="")
    elif flag == 2:
        #Poland
        screen = Canvas(root, width=400, height= 300, bg="white")
        screen.create_rectangle(0,150,400,300, fill="red")
    elif flag == 3:
        #Trans
        screen = Canvas(root, width=640, height=480, background="#00f0ff")
        screen.create_rectangle(0,96,640,192, fill="#ff5bf3", outline="")
        screen.create_rectangle(0,192,640,288, fill="white", outline="")
        screen.create_rectangle(0,288,640,384, fill="#ff5bf3", outline="")
    elif flag == 4:
        #Aroace
        screen =  Canvas(root, width=640, height=480, bg ="white")
        screen.create_rectangle(0,0,640,96, fill="#ef9007", outline="")
        screen.create_rectangle(0,96,640,192, fill="#f6d317", outline="")
        screen.create_rectangle(0,288,640,384, fill="#45bcee", outline="")
        screen.create_rectangle(0,384,640,480, fill="#1e3f54", outline="")
    else:
        root.quit()
    screen.pack()

#Setup
flag=-1
root = Tk()
flags = ["Random","North Macedonia","Poland", "Secret", "Secret2","Exit"]
X=len(flags-1)

#display buttons
for i in range(len(flags)):
    button = Button(root, text=flags[i], command= lambda i = i: button_click(i))
    button.pack(pady=5)

mainloop()
