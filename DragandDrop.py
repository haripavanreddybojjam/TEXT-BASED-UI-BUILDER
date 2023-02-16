import tkinter as tk

ele = ["Label", "Button"]
w=800
h=600

def drag_start(event):

    l1 = event.widget
    try:
        l1.startX = event.x
        l1.startY = event.y

    except AttributeError:
        pass

def drag_motion(event):

    l1 = event.widget
    try:
        x = l1.winfo_x() - l1.startX + event.x
        y = l1.winfo_y() - l1.startY + event.y
        l1.place(x=x, y=y)
    except AttributeError:
        pass



samp = tk.Tk()
samp.title("UI BUilder")
samp.geometry(f'{w}x{h}')
samp.resizable(0,0)


l2 = tk.Label(samp, bg="blue", width=10, height=5)
l2.place(x=100, y=100)
l2.bind("<Button-1>", drag_start)
l2.bind("<B1-Motion>", drag_motion)

def get_info():
    print(l2.winfo_x())
    print(l2.winfo_geometry())

b1=tk.Button(samp,text="Get Info",command=get_info)
b1.place(x=25,y=0)
l1 = tk.Label(samp, text="Hello Amrita", width=10, height=5)
l1.place(x=0, y=0)
l1.bind("<Button-1>", drag_start)
l1.bind("<B1-Motion>", drag_motion)



l3 = tk.Entry(samp,  width=10)
l3.place(x=100, y=100)
l3.bind("<Button-1>", drag_start)
l3.bind("<B1-Motion>", drag_motion)

l4 = tk.Button(samp,  width=10, height=5)
l4.place(x=100, y=100)
l4.bind("<Button-1>", drag_start)
l4.bind("<B1-Motion>", drag_motion)

l5 = tk.Radiobutton(samp, width=10, height=5)
l5.place(x=100, y=100)
l5.bind("<Button-1>", drag_start)
l5.bind("<B1-Motion>", drag_motion)

l6 = tk.Checkbutton(samp, width=10, height=5)
l6.place(x=100, y=100)
l6.bind("<Button-1>", drag_start)
l6.bind("<B1-Motion>", drag_motion)

l7 = tk.Scale(samp,  width=10)
l7.place(x=100, y=100)
l7.bind("<Button-1>", drag_start)
l7.bind("<B1-Motion>", drag_motion)

l8 = tk.Scrollbar(samp, width=10)
l8.place(x=100, y=100)
l8.bind("<Button-1>", drag_start)
l8.bind("<B1-Motion>", drag_motion)

samp.mainloop()
