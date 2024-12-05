from tkinter import *

root = Tk()
flags = ["North Macedonia (NM)","Poland (P)", "Secret (T)", "Secret2 (AA)"]
print(flags)
flag = input("Please select the flag you would like to print: ")
if flag == "NM":
    screen = Canvas(root, width=400, height=300, bg="red")
    #shapes
    screen.create_polygon(0,0,200,150,80,0,0,0, fill="yellow")
    screen.create_polygon(175,0,200,150,225,0,175,0, fill="yellow")
    screen.create_polygon(400,0,200,150,320,0,400,0, fill="yellow")
    screen.create_polygon(0,125,200,150,0,175,0,125, fill="yellow")
    screen.create_polygon(0,300,200,150,80,300,0,300, fill="yellow")
    screen.create_polygon(175,300,200,150,225,300,175,300, fill="yellow")
    screen.create_polygon(400,300,200,150,320,300,400,300, fill="yellow")
    screen.create_polygon(400,125,200,150,400,175,400,175, fill="yellow")
    screen.create_oval(170,120,230,180, fill="yellow", outline="")
elif flag == "P":
    screen = Canvas(root, width=400, height= 300, bg="white")
    screen.create_rectangle(0,150,400,300, fill="red")
elif flag == "T":
    screen = Canvas(root, width=640, height=480, background="#00f0ff")
    screen.create_rectangle(0,96,640,192, fill="#ff5bf3", outline="")
    screen.create_rectangle(0,192,640,288, fill="white", outline="")
    screen.create_rectangle(0,288,640,384, fill="#ff5bf3", outline="")
elif flag == "AA":
    screen =  Canvas(root, width=640, height=480, bg ="white")
    screen.create_rectangle(0,0,640,96, fill="#ef9007", outline="")
    screen.create_rectangle(0,96,640,192, fill="#f6d317", outline="")
    screen.create_rectangle(0,288,640,384, fill="#45bcee", outline="")
    screen.create_rectangle(0,384,640,480, fill="#1e3f54", outline="")
screen.pack()
mainloop()