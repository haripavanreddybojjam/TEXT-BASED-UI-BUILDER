import tkinter as tk
from tkinter import ttk
ele = ["ButtOn","button","radiobutton","entry","checkbutton","scALe","scrollbar","scale"]
w=800
h=600

allow_dd=0

samp = tk.Tk()
samp.title("UI BUilder")
samp.geometry(f'{w}x{h}')
samp.resizable(0,0)

x={}

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


for i in range(len(ele)):
    if ele[i].lower()=="button":
        a = f'x{i}'
        globals()[a]=tk.Button()
        x[a]=tk.Button(samp,text="Sample Text Here!")
    if ele[i].lower()=="entry":
        a = f'x{i}'
        globals()[a]=tk.Entry(samp,text="Sample Text Here!",width=10)
        x[a]=tk.Entry(samp,text="Sample Text Here!",width=10)
    if ele[i].lower()=="radiobutton":
        a = f'x{i}'
        globals()[a]=tk.Radiobutton(samp)
        x[a]=tk.Radiobutton(samp)
    if ele[i].lower()=="checkbutton":
        a = f'x{i}'
        globals()[a]=tk.Checkbutton(samp)
        x[a]=tk.Checkbutton(samp)
    if ele[i].lower()=="scale":
        a = f'x{i}'
        globals()[a] = tk.Scale(samp)
        x[a] = tk.Scale(samp)

    if ele[i].lower()=="scrollbar":
        a = f'x{i}'
        globals()[a] = tk.Scrollbar(samp)
        x[a] = tk.Scrollbar(samp)

    if ele[i].lower()=="combobox":
        a = f'x{i}'
        globals()[a] = ttk.Combobox(samp)
        x[a] = ttk.Combobox(samp)

    if ele[i].lower()=="spinbox":
        a = f'x{i}'
        globals()[a] = tk.Spinbox(samp)
        x[a] = tk.Spinbox(samp)

for i in range(len(ele)):
    x[f'x{i}'].place(x=i*50+50,y=i*50+50)



def on_enable():
    global allow_dd
    main_button.configure(text="Disable Drag Drop",bg="Green",fg="white",font=('Bahnschrift', 13, 'bold'), border=0)
    allow_dd = 1
    for i in range(len(ele)):
        x[f'x{i}'].bind("<Button-1>", drag_start)
        x[f'x{i}'].bind("<B1-Motion>", drag_motion)
        print(x[f'x{i}'].winfo_x())
        print(x[f'x{i}'].winfo_y())
        print(f"x{i}===========================================")

def on_disable():
    global allow_dd
    main_button.configure(text="Enble Drag Drop", bg="Red", fg="white", font=('Bahnschrift', 13, 'bold'), border=0)
    allow_dd = 0
    for i in range(len(ele)):
        x[f'x{i}'].unbind("<Button-1>")
        x[f'x{i}'].unbind("<B1-Motion>")
        print(x[f'x{i}'].winfo_x())
        print(x[f'x{i}'].winfo_y())
        print(f"x{i}===========================================")


def on_click_drag_drop():
    global allow_dd
    if allow_dd==1:
        on_disable()
    else:
        on_enable()
main_button=tk.Button(samp,text="Enable Drag and Drop",command=on_click_drag_drop)
main_button.place(x=400,y=0)
samp.mainloop()
