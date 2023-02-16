'''


Font family list

'''
import json
import ast
with open('main_details.json') as f:
   datas = json.load(f)


root_path=datas['Root_path']
user=datas['User']
file=root_path+'/basic_details.json'
try:
    with open(file,'r') as f:
        va = json.load(f)
except FileNotFoundError:
    va={'bg':"white",'width':500,'height':500}



print(va)
font_fams=[
"Terminal",
"Fixedsys",
"Modern",
"Roman",
"Script",
"Courier",
"MS Serif",
"MS Sans Serif",
"Small Fonts",
"Verdana"
]

cursors = ['arrow', 'man', 'based_arrow_down', 'middlebutton', 'based_arrow_up', 'mouse', 'boat', 'pencil', 'bogosity', 'pirate', 'bottom_left_corner', 'plus', 'bottom_right_corner', 'question_arrow', 'bottom_side', 'right_ptr', 'bottom_tee', 'right_side', 'box_spiral', 'right_tee', 'center_ptr', 'rightbutton', 'circle', 'rtl_logo', 'clock', 'sailboat', 'coffee_mug', 'sb_down_arrow', 'cross', 'sb_h_double_arrow', 'cross_reverse', 'sb_left_arrow', 'crosshair', 'sb_right_arrow', 'diamond_cross',
           'sb_up_arrow', 'dot', 'sb_v_double_arrow', 'dotbox', 'shuttle', 'double_arrow', 'sizing', 'draft_large', 'spider', 'draft_small', 'spraycan', 'draped_box', 'star', 'exchange', 'target', 'fleur', 'tcross', 'gobbler', 'top_left_arrow', 'gumby', 'top_left_corner', 'hand1', 'top_right_corner', 'hand2', 'top_side', 'heart', 'top_tee', 'icon', 'trek', 'iron_cross', 'ul_angle', 'left_ptr', 'umbrella', 'left_side', 'ur_angle', 'left_tee', 'watch', 'leftbutton', 'xterm', 'll_angle', 'X_cursor', 'lr_angle']


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk,ImageOps
images_list={}
images_path={}
allow_dd=0

root=tk.Tk()
root.geometry('1080x720')
root.minsize(1080,720)
root.title("UI Builder")

x={}
#ele = ["Button","button","radiobutton","entry","checkbutton","scALe","scrollbar","scale"]
ele=["Scale","entry","text","Button","radiobutton"]
def on_gen():
    pass
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

    main_button.configure(text="Enable Drag Drop", bg="Red", fg="white", font=('Bahnschrift', 13, 'bold'), border=0)
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


top_frame=tk.Frame(root,bg='#2b72cf',height=80,width=2500)
top_frame=tk.Frame(root,bg='#2b72cf',height=80,width=2500)
top_frame.place(x=0,y=0)

lab_UI=tk.Label(text="UI Builder",font=('Bahnschrift',24),bg="#2b72cf",fg='white')
lab_UI.place(x=900,y=20)

lab_Uname=tk.Label(text=f"Welcome, {user}!",font=('Bahnschrift',20),bg="#2b72cf",fg='white')
lab_Uname.place(x=20,y=5)

logout=tk.Button(top_frame,text="Logout", font=('Bahnschrift',12),command='',border=0,bg="#2b72cf",fg='white')
logout.place(x=20,y=45)

changepass=tk.Button(top_frame,text="Change Password",command='', font=('Bahnschrift',12),border=0,bg="#2b72cf",fg='white')
changepass.place(x=100,y=45)

editing_frame=tk.Frame(root,bg='black',height=1500,width=2500)
editing_frame.place(x=279,y=81)

samp_frame=tk.Frame(editing_frame,width=int(va['width']),height=int(va['height']),bg=va['bg'])
samp_frame.place(x=10,y=8)

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
        x[a]=tk.Button(samp_frame,text="Sample Text Here!")
    if ele[i].lower()=="entry":
        a = f'x{i}'
        globals()[a]=tk.Entry(samp_frame,text="Sample Text Here!",width=10)
        x[a]=tk.Entry(samp_frame,text="Sample Text Here!",width=10)
    if ele[i].lower()=="radiobutton":
        a = f'x{i}'
        globals()[a]=tk.Radiobutton(samp_frame)
        x[a]=tk.Radiobutton(samp_frame)
    if ele[i].lower()=="checkbutton":
        a = f'x{i}'
        globals()[a]=tk.Checkbutton(samp_frame)
        x[a]=tk.Checkbutton(samp_frame)
    if ele[i].lower()=="text":
        a = f'x{i}'
        globals()[a]=tk.Label(samp_frame)
        x[a]=tk.Label(samp_frame,text="sample text")
    if ele[i].lower()=="scale":
        a = f'x{i}'
        globals()[a] = tk.Scale(samp_frame)
        x[a] = tk.Scale(samp_frame)

    if ele[i].lower()=="scrollbar":
        a = f'x{i}'
        globals()[a] = tk.Scrollbar(samp_frame)
        x[a] = tk.Scrollbar(samp_frame)

    if ele[i].lower()=="combobox":
        a = f'x{i}'
        globals()[a] = ttk.Combobox(samp_frame)
        x[a] = ttk.Combobox(samp_frame)

    if ele[i].lower()=="spinbox":
        a = f'x{i}'
        globals()[a] = tk.Spinbox(samp_frame)
        x[a] = tk.Spinbox(samp_frame)
    if ele[i].lower() == "image":
        a = f'x{i}'
        globals()[a] = tk.Button(samp_frame,border=0)
        x[a]=tk.Button(samp_frame,border=0)
        imgb = Image.open("sample.jpg")
        img_resized = imgb.resize((250,250))
        imgb = ImageTk.PhotoImage(img_resized)
        x[a].configure(image=imgb)


for i in range(len(ele)):
    x[f'x{i}'].place(x=i*50+50,y=i*50+50)

update_frame=tk.Frame(root,bg='#7ab541',height=800,width=278)
update_frame.place(x=0,y=81)

text_frame=tk.Frame(update_frame,bg='#10535b',width=278,height=244)
text_frame.place(x=0,y=0)

upload_im=tk.Label(text_frame,text="Upload Requirements Text Below",bg='#10535b',fg='white',font=('Bahnschrift',13))
upload_im.place(x=10,y=7)


in_text=tk.Text(text_frame, width=32, height=8)
in_text.place(x=10,y=70)


upload_button=tk.Button(text_frame,command=on_gen,text="Generate",border=0,width=10)
upload_button.place(x=100,y=40)

allow_frame=tk.Frame(update_frame,bg='#10535b',width=278,height=45)
allow_frame.place(x=0,y=250)

main_button=tk.Button(allow_frame,text="Enable Drag and Drop",width=25,command=on_click_drag_drop,bg="Red", fg="white", font=('Bahnschrift', 13, 'bold'), border=0)
main_button.place(x=20,y=5)

basicprop_frame=tk.Frame(update_frame,bg='#10535b',width=278,height=250)
basicprop_frame.place(x=0,y=300)

Lab_Basic_prop_title=tk.Label(basicprop_frame,text="Basic Properties",font=('Bahnschrift',14,'bold','underline'),bg='#10535b',fg='white')
Lab_Basic_prop_title.place(x=53,y=8)

def on_get_wid_props():
    global font_fams
    scree=messagebox.askyesno("UI Builder", "Do you want to update the resolution of screen?")
    if scree==1:
        top = tk.Toplevel()
        top.geometry("300x400")
        top.resizable(0, 0)
        top.title("Widget Update")
        BG = tk.Label(top, text="Background", font=('Bahnschrift', 10))
        BG.place(x=15, y=10)
        bg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
        bg_in.insert(0,samp_frame['bg'])
        bg_in.place(x=100, y=10)
        x_res = tk.Label(top, text="X Resolution", font=('Bahnschrift', 10))
        x_res.place(x=15, y=40)
        x_res_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
        x_res_in.insert(0, samp_frame['width'])
        x_res_in.place(x=100, y=40)
        y_res = tk.Label(top, text="Y Resolution", font=('Bahnschrift', 10))
        y_res.place(x=15, y=70)
        y_res_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
        y_res_in.insert(0, samp_frame['height'])
        y_res_in.place(x=100, y=70)
        titl_e = tk.Label(top, text="Title :", font=('Bahnschrift', 10))
        titl_e.place(x=15, y=100)
        titl_e_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
        titl_e_in.place(x=100, y=100)
        def on_upd_res():
            samp_frame['bg']=bg_in.get()
            samp_frame['width']=int(x_res_in.get())
            samp_frame['height'] = int(y_res_in.get())
            with open(root_path+'/basic_details.json', 'w') as f:
                user_data={'bg':bg_in.get(),'width':int(x_res_in.get()),'height':int(y_res_in.get()),'title':titl_e_in.get()}
                json.dump(user_data, f)

        scr_upd = tk.Button(top, command=on_upd_res, text="Update",
                                      bg="green", fg="white", font=('Bahnschrift', 13, 'bold'), border=0)
        scr_upd.place(x=70, y=150)

        top.mainloop()

    else:
        oth_pro=messagebox.askyesno("UI Builder","Updating widget Properties?")
        if oth_pro==1:
            a=list(x)

            for i in a:

                if x[i].widgetName=='button':
                    a=x[i]['activebackground']
                    x[i].configure(activebackground = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow','magenta']))
                    x[i].flash()
                    time.sleep(0.5)
                    x[i].configure(
                        activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
                    x[i].flash()
                    time.sleep(0.5)
                    x[i].configure(activebackground=a)
                    a=messagebox.askyesno("UI Builder","Do you want to update the flashing widget")

                    if a==1:
                        top = tk.Toplevel()
                        top.geometry("300x400")
                        top.resizable(0, 0)
                        top.title("Widget Update")
                        BG=tk.Label(top,text="Background",font=('Bahnschrift', 10))
                        BG.place(x=15,y=10)
                        bg_in=tk.Entry(top,font=('Bahnschrift', 10),width=25)
                        bg_in.insert(0,x[i]['bg'])
                        bg_in.place(x=100,y=10)
                        FG = tk.Label(top, text="Foreground", font=('Bahnschrift', 10))
                        FG.place(x=15, y=40)
                        fg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fg_in.insert(0, x[i]['fg'])
                        fg_in.place(x=100, y=40)
                        txt = tk.Label(top, text="Text ", font=('Bahnschrift', 10))
                        txt.place(x=15, y=70)
                        txt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        txt_in.insert(0, x[i]['text'])
                        txt_in.place(x=100, y=70)
                        borde_r = tk.Label(top, text="Border ", font=('Bahnschrift', 10))
                        borde_r.place(x=15, y=100)
                        border_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        border_in.insert(0, x[i]['border'])
                        border_in.place(x=100, y=100)
                        pad_x = tk.Label(top, text="pad x: ", font=('Bahnschrift', 10))
                        pad_x.place(x=15, y=130)
                        px_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        px_in.insert(0, x[i]['padx'])
                        px_in.place(x=100, y=130)
                        pad_y = tk.Label(top, text="pad y: ", font=('Bahnschrift', 10))
                        pad_y.place(x=15, y=160)
                        py_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        py_in.insert(0, x[i]['pady'])
                        py_in.place(x=100, y=160)
                        fnt = tk.Label(top, text="Font Size: ", font=('Bahnschrift', 10))
                        fnt.place(x=15, y=190)
                        fnt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fnt_in.insert(0, 10)
                        fnt_in.place(x=100, y=190)
                        fnt_fam = tk.Label(top, text="Font family: ", font=('Bahnschrift', 10))
                        fnt_fam.place(x=15, y=220)
                        fntf_in = ttk.Combobox(top,values=font_fams, text="Font Size: ", font=('Bahnschrift', 10))
                        fntf_in.insert(0, x[i]['font'])
                        fntf_in.place(x=100, y=220)
                        x_res = tk.Label(top, text=" X res: ", font=('Bahnschrift', 10))
                        x_res.place(x=15, y=250)
                        x_res_in = tk.Entry(top, font=('Bahnschrift', 10), width=5)
                        x_res_in.place(x=100, y=250)
                        y_res = tk.Label(top, text=" Y res: ", font=('Bahnschrift', 10))
                        y_res.place(x=15, y=280)
                        y_res_in = tk.Entry(top, font=('Bahnschrift', 10), width=5)
                        y_res_in.place(x=100, y=280)

                        def on_upl():
                            try:
                                global images_list
                                f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
                                filename = filedialog.askopenfilename(filetypes=f_types)
                                print(filename)

                                images_list[f"{i}"] = ImageTk.PhotoImage(Image.open(filename).resize((int(x_res_in.get()), int(y_res_in.get()))))

                                x[i].configure(image=images_list[f"{i}"])


                            except Exception:
                                messagebox.showinfo("UI Builder", "Enter Size of image")

                        img_in = tk.Button(top, command=on_upl, text="Select Image", width=15, font=('Bahnschrift', 10))
                        img_in.place(x=100, y=310)


                        def upds():
                            try:
                                bgn=bg_in.get()
                                fgn=fg_in.get()
                                bordern=border_in.get()
                                txtn=txt_in.get()
                                padxn=px_in.get()
                                padyn=py_in.get()
                                fntf=fntf_in.get()
                                x[i]['bg']=bgn
                                x[i]['fg'] = fgn
                                x[i]['border'] = bordern
                                x[i]['text'] = txtn
                                x[i]['padx'] = padxn
                                x[i]['pady'] = padyn
                                x[i].configure(font=(str(fntf), int(fnt_in.get()),))

                            except Exception :
                                messagebox.showinfo("UI Builder","Re Check Your inputs and try again")
                            finally:
                                return 0
                        upd=tk.Button(top,text="Update",command=upds,bg="green", fg="white", font=('Bahnschrift', 13), border=0)
                        upd.place(x=120,y=340)
                        top.mainloop()
                        break
                    if a==0:
                        pass
                if x[i].widgetName=='label':
                    content = x[i]['bg']
                    x[i].configure(bg="red")
                    time.sleep(1)
                    a = messagebox.askyesno("UI Builder", "Do you want to update the Red Text Box  ?")

                    if a==1:
                        x[i].configure(bg=content)
                        top = tk.Toplevel()
                        top.geometry("300x400")
                        top.resizable(0, 0)
                        top.title("Widget Update")
                        BG=tk.Label(top,text="Background",font=('Bahnschrift', 10))
                        BG.place(x=15,y=10)
                        bg_in=tk.Entry(top,font=('Bahnschrift', 10),width=25)
                        bg_in.insert(0,x[i]['bg'])
                        bg_in.place(x=100,y=10)
                        FG = tk.Label(top, text="Foreground", font=('Bahnschrift', 10))
                        FG.place(x=15, y=40)
                        fg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fg_in.insert(0, x[i]['fg'])
                        fg_in.place(x=100, y=40)
                        txt = tk.Label(top, text="Text ", font=('Bahnschrift', 10))
                        txt.place(x=15, y=70)
                        txt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        txt_in.insert(0, x[i]['text'])
                        txt_in.place(x=100, y=70)
                        borde_r = tk.Label(top, text="Border ", font=('Bahnschrift', 10))
                        borde_r.place(x=15, y=100)
                        border_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        border_in.insert(0, x[i]['border'])
                        border_in.place(x=100, y=100)
                        pad_x = tk.Label(top, text="pad x: ", font=('Bahnschrift', 10))
                        pad_x.place(x=15, y=130)
                        px_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        px_in.insert(0, x[i]['padx'])
                        px_in.place(x=100, y=130)
                        pad_y = tk.Label(top, text="pad y: ", font=('Bahnschrift', 10))
                        pad_y.place(x=15, y=160)
                        py_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        py_in.insert(0, x[i]['pady'])
                        py_in.place(x=100, y=160)
                        fnt = tk.Label(top, text="Font Size: ", font=('Bahnschrift', 10))
                        fnt.place(x=15, y=190)
                        fnt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fnt_in.insert(0, 10)
                        fnt_in.place(x=100, y=190)
                        fnt_fam = tk.Label(top, text="Font family: ", font=('Bahnschrift', 10))
                        fnt_fam.place(x=15, y=220)
                        fntf_in = ttk.Combobox(top,values=font_fams, text="Font Size: ", font=('Bahnschrift', 10))
                        fntf_in.insert(0, x[i]['font'])
                        fntf_in.place(x=100, y=220)

                        def upds():
                            try:
                                bgn=bg_in.get()
                                fgn=fg_in.get()
                                bordern=border_in.get()
                                txtn=txt_in.get()
                                padxn=px_in.get()
                                padyn=py_in.get()
                                fntf=fntf_in.get()
                                x[i]['bg']=bgn
                                x[i]['fg'] = fgn
                                x[i]['border'] = bordern
                                x[i]['text'] = txtn
                                x[i]['padx'] = padxn
                                x[i]['pady'] = padyn
                                x[i].configure(font=(str(fntf), int(fnt_in.get()),))

                            except Exception :
                                messagebox.showinfo("UI Builder","Re Check Your inputs and try again")
                            finally:
                                return 0
                        upd=tk.Button(top,text="Update",command=upds,bg="green", fg="white", font=('Bahnschrift', 13), border=0)
                        upd.place(x=120,y=340)
                        top.mainloop()
                        break
                    if a==0:
                        x[i].configure(bg=content)
                if x[i].widgetName=='entry':
                    content=x[i]['bg']
                    x[i].configure(bg="red")
                    time.sleep(1)
                    a = messagebox.askyesno("UI Builder", "Do you want to update the Red Text Box  ?")

                    if a==1:
                        x[i].configure(bg=content)
                        top = tk.Toplevel()
                        top.geometry("300x350")
                        top.resizable(0, 0)
                        top.title("Widget Update")
                        BG=tk.Label(top,text="Background",font=('Bahnschrift', 10))
                        BG.place(x=15,y=10)
                        bg_in=tk.Entry(top,font=('Bahnschrift', 10),width=25)
                        bg_in.insert(0,x[i]['bg'])
                        bg_in.place(x=100,y=10)
                        FG = tk.Label(top, text="Foreground", font=('Bahnschrift', 10))
                        FG.place(x=15, y=40)
                        fg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fg_in.insert(0, x[i]['fg'])
                        fg_in.place(x=100, y=40)
                        curso_r = tk.Label(top, text="Cursor", font=('Bahnschrift', 10))
                        curso_r.place(x=15, y=70)
                        cursor_in = ttk.Combobox(top, values=cursors, text="Font Size: ", font=('Bahnschrift', 10))
                        cursor_in.insert(0,x[i]['cursor'])
                        cursor_in.place(x=100, y=70)
                        borde_r = tk.Label(top, text="Border :", font=('Bahnschrift', 10))
                        borde_r.place(x=15, y=100)
                        borde_r_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        borde_r_in.insert(0, x[i]['border'])
                        borde_r_in.place(x=100, y=100)
                        widt_h = tk.Label(top, text="Width :", font=('Bahnschrift', 10))
                        widt_h.place(x=15, y=130)
                        widt_h_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        widt_h_in.insert(0, x[i]['width'])
                        widt_h_in.place(x=100, y=130)
                        fontsize = tk.Label(top, text="Font  :", font=('Bahnschrift', 10))
                        fontsize.place(x=15, y=160)
                        fontsize_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fontsize_in.insert(0,10)
                        fontsize_in.place(x=100, y=160)
                        fontfam = tk.Label(top, text="Font family :", font=('Bahnschrift', 10))
                        fontfam.place(x=15, y=190)
                        fontfam_in = ttk.Combobox(top,values=["Terminal","Fixedsys","Modern","Roman","Script", "Courier",
                                                              "MS Serif","MS Sans Serif","Small Fonts","Verdana"],font=('Bahnschrift', 10), width=25)

                        fontfam_in.place(x=100, y=190)


                        def upds():
                            try:
                                bgn=bg_in.get()
                                curn=cursor_in.get()
                                x[i]['bg']=bgn
                                x[i]['fg'] = fg_in.get()
                                x[i]['cursor']=curn
                                x[i]['border']=int(borde_r_in.get())
                                x[i]['width'] = int(widt_h_in.get())
                                x[i].configure(font=(f" {fontfam_in.get()} {int(fontsize_in.get())}"))
                            except Exception :
                                print(Exception)
                                messagebox.showinfo("UI Builder","Re Check Your inputs and try again")
                            finally:
                                return 0
                        upd=tk.Button(top,text="Update",command=upds,bg="green", fg="white", font=('Bahnschrift', 13), border=0)
                        upd.place(x=120,y=300)
                        top.mainloop()
                        break
                    if a==0:
                        x[i].configure(bg=content)
                        pass
                if x[i].widgetName=='scale':
                    content=x[i]['bg']
                    x[i].configure(bg="red")
                    time.sleep(1)
                    a = messagebox.askyesno("UI Builder", "Do you want to update the Red Scale  ?")

                    if a==1:
                        x[i].configure(bg=content)
                        top = tk.Toplevel()
                        top.geometry("300x550")
                        top.resizable(0, 0)
                        top.title("Widget Update")
                        BG=tk.Label(top,text="Background",font=('Bahnschrift', 10))
                        BG.place(x=15,y=10)
                        bg_in=tk.Entry(top,font=('Bahnschrift', 10),width=25)
                        bg_in.insert(0,x[i]['bg'])
                        bg_in.place(x=100,y=10)
                        FG = tk.Label(top, text="Foreground", font=('Bahnschrift', 10))
                        FG.place(x=15, y=40)
                        fg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fg_in.insert(0, x[i]['fg'])
                        fg_in.place(x=100, y=40)
                        curso_r = tk.Label(top, text="Cursor", font=('Bahnschrift', 10))
                        curso_r.place(x=15, y=70)
                        cursor_in = ttk.Combobox(top, values=cursors, text="Font Size: ", font=('Bahnschrift', 10))
                        cursor_in.insert(0,x[i]['cursor'])
                        cursor_in.place(x=100, y=70)
                        borde_r = tk.Label(top, text="Border :",     font=('Bahnschrift', 10))
                        borde_r.place(x=15, y=100)
                        borde_r_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        borde_r_in.insert(0, x[i]['border'])
                        borde_r_in.place(x=100, y=100)
                        widt_h = tk.Label(top, text="Width :", font=('Bahnschrift', 10))
                        widt_h.place(x=15, y=130)
                        widt_h_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        widt_h_in.insert(0, x[i]['width'])
                        widt_h_in.place(x=100, y=130)
                        lengt_h = tk.Label(top, text="Length :", font=('Bahnschrift', 10))
                        lengt_h.place(x=15, y=160)
                        lengt_h_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        lengt_h_in.insert(0, x[i]['length'])
                        lengt_h_in.place(x=100, y=160)
                        fontsize = tk.Label(top, text="Font  :", font=('Bahnschrift', 10))
                        fontsize.place(x=15, y=190)
                        fontsize_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fontsize_in.insert(0,8)
                        fontsize_in.place(x=100, y=190)
                        fontfam = tk.Label(top, text="Font family :", font=('Bahnschrift', 10))
                        fontfam.place(x=15, y=220)
                        fontfam_in = ttk.Combobox(top,values=["Terminal","Fixedsys","Modern","Roman","Script", "Courier",
                                                              "MS Serif","MS Sans Serif","Small Fonts","Verdana"],font=('Bahnschrift', 10), width=25)

                        fontfam_in.place(x=100, y=220)
                        from_val = tk.Label(top, text="From  :", font=('Bahnschrift', 10))
                        from_val.place(x=15, y=250)
                        from_val_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        from_val_in.place(x=100, y=250)
                        to_val = tk.Label(top, text="To  :", font=('Bahnschrift', 10))
                        to_val.place(x=15, y=280)
                        to_val_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        to_val_in.place(x=100, y=280)
                        orients = tk.Label(top, text="orientation :", font=('Bahnschrift', 10))
                        orients.place(x=15, y=310)
                        orients_in = ttk.Combobox(top, values=["Horizontal", "Vertical"], font=('Bahnschrift', 10),
                                                  width=25)

                        orients_in.place(x=100, y=310)

                        def upds():
                            try:
                                bgn=bg_in.get()
                                curn=cursor_in.get()
                                x[i]['bg']=bgn
                                x[i]['fg'] = fg_in.get()
                                x[i]['cursor']=curn
                                x[i]['border']=int(borde_r_in.get())
                                x[i]['width'] = int(widt_h_in.get())
                                x[i]['length'] = int(lengt_h_in.get())
                                x[i].configure(font=(f" {fontfam_in.get()} {int(fontsize_in.get())}"))
                                x[i].configure(from_=int(from_val_in.get()),to=int(to_val_in.get()))
                                if orients_in.get()=="Horizontal":
                                    x[i].configure(orient=tk.HORIZONTAL)
                                else:
                                    x[i].configure(orient=tk.VERTICAL)
                            except Exception :
                                print(Exception)
                                messagebox.showinfo("UI Builder","Re Check Your inputs and try again")
                            finally:
                                return 0
                        upd=tk.Button(top,text="Update",command=upds,bg="green", fg="white", font=('Bahnschrift', 13), border=0)
                        upd.place(x=120,y=350)
                        top.mainloop()
                        break
                    if a==0:
                        x[i].configure(bg=content)
                        pass
                if x[i].widgetName=='checkbutton':
                    a=x[i]['activebackground']
                    x[i].configure(activebackground = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow','magenta']))
                    x[i].flash()
                    time.sleep(0.5)
                    x[i].configure(
                        activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
                    x[i].flash()
                    time.sleep(0.5)
                    x[i].configure(activebackground=a)
                    a=messagebox.askyesno("UI Builder","Do you want to update the flashing widget")

                    if a==1:
                        top = tk.Toplevel()
                        top.geometry("300x400")
                        top.resizable(0, 0)
                        top.title("Widget Update")
                        BG=tk.Label(top,text="Background",font=('Bahnschrift', 10))
                        BG.place(x=15,y=10)
                        bg_in=tk.Entry(top,font=('Bahnschrift', 10),width=25)
                        bg_in.insert(0,x[i]['bg'])
                        bg_in.place(x=100,y=10)
                        FG = tk.Label(top, text="Foreground", font=('Bahnschrift', 10))
                        FG.place(x=15, y=40)
                        fg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fg_in.insert(0, x[i]['fg'])
                        fg_in.place(x=100, y=40)
                        txt = tk.Label(top, text="Text ", font=('Bahnschrift', 10))
                        txt.place(x=15, y=70)
                        txt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        txt_in.insert(0, x[i]['text'])
                        txt_in.place(x=100, y=70)
                        borde_r = tk.Label(top, text="Border ", font=('Bahnschrift', 10))
                        borde_r.place(x=15, y=100)
                        border_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        border_in.insert(0, x[i]['border'])
                        border_in.place(x=100, y=100)
                        pad_x = tk.Label(top, text="pad x: ", font=('Bahnschrift', 10))
                        pad_x.place(x=15, y=130)
                        px_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        px_in.insert(0, x[i]['padx'])
                        px_in.place(x=100, y=130)
                        pad_y = tk.Label(top, text="pad y: ", font=('Bahnschrift', 10))
                        pad_y.place(x=15, y=160)
                        py_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        py_in.insert(0, x[i]['pady'])
                        py_in.place(x=100, y=160)
                        fnt = tk.Label(top, text="Font Size: ", font=('Bahnschrift', 10))
                        fnt.place(x=15, y=190)
                        fnt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fnt_in.insert(0, 10)
                        fnt_in.place(x=100, y=190)
                        fnt_fam = tk.Label(top, text="Font family: ", font=('Bahnschrift', 10))
                        fnt_fam.place(x=15, y=220)
                        fntf_in = ttk.Combobox(top,values=font_fams, text="Font Size: ", font=('Bahnschrift', 10))
                        fntf_in.insert(0, x[i]['font'])
                        fntf_in.place(x=100, y=220)
                        img_ = tk.Label(top, text="Image (if any): ", font=('Bahnschrift', 10))
                        img_.place(x=15, y=250)
                        x_res = tk.Label(top, text=" X res: ", font=('Bahnschrift', 10))
                        x_res.place(x=15, y=280)
                        x_res_in=tk.Entry(top, font=('Bahnschrift', 10), width=5)
                        x_res_in.place(x=100,y=280)
                        y_res = tk.Label(top, text=" Y res: ", font=('Bahnschrift', 10))
                        y_res.place(x=15, y=310)
                        y_res_in = tk.Entry(top, font=('Bahnschrift', 10), width=5)
                        y_res_in.place(x=100, y=310)
                        def on_upl():
                            try:
                                global images_list
                                f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
                                filename = filedialog.askopenfilename(filetypes=f_types)
                                print(filename)

                                images_list[f"{i}"] = ImageTk.PhotoImage(Image.open(filename).resize((int(x_res_in.get()), int(y_res_in.get()))))

                                x[i].configure(image=images_list[f"{i}"])
                            except Exception:
                                messagebox.showinfo("UI Builder","Enter Size of image")

                        img_in = tk.Button(top, command=on_upl, text="Select Image", width=15, font=('Bahnschrift', 10))
                        img_in.place(x=100, y=250)
                        def upds():
                            try:
                                bgn=bg_in.get()
                                fgn=fg_in.get()
                                bordern=border_in.get()
                                txtn=txt_in.get()
                                padxn=px_in.get()
                                padyn=py_in.get()
                                fntf=fntf_in.get()
                                x[i].deselect()
                                x[i]['bg']=bgn
                                x[i]['fg'] = fgn
                                x[i]['border'] = bordern
                                x[i]['text'] = txtn
                                x[i]['padx'] = padxn
                                x[i]['pady'] = padyn
                                x[i].configure(font=(str(fntf), int(fnt_in.get()),))
                            except Exception :
                                messagebox.showinfo("UI Builder","Re Check Your inputs and try again")
                            finally:
                                return 0
                        upd=tk.Button(top,text="Update",command=upds,bg="green", fg="white", font=('Bahnschrift', 13), border=0)
                        upd.place(x=120,y=340)
                        top.mainloop()
                        break
                    if a==0:
                        pass
                if x[i].widgetName=='radiobutton':
                    a=x[i]['activebackground']
                    x[i].configure(activebackground = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow','magenta']))
                    x[i].flash()
                    time.sleep(0.5)
                    x[i].configure(
                        activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
                    x[i].flash()
                    time.sleep(0.5)
                    x[i].configure(activebackground=a)
                    a=messagebox.askyesno("UI Builder","Do you want to update the flashing widget")

                    if a==1:
                        top = tk.Toplevel()
                        top.geometry("300x400")
                        top.resizable(0, 0)
                        top.title("Widget Update")
                        BG=tk.Label(top,text="Background",font=('Bahnschrift', 10))
                        BG.place(x=15,y=10)
                        bg_in=tk.Entry(top,font=('Bahnschrift', 10),width=25)
                        bg_in.insert(0,x[i]['bg'])
                        bg_in.place(x=100,y=10)
                        FG = tk.Label(top, text="Foreground", font=('Bahnschrift', 10))
                        FG.place(x=15, y=40)
                        fg_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fg_in.insert(0, x[i]['fg'])
                        fg_in.place(x=100, y=40)
                        txt = tk.Label(top, text="Text ", font=('Bahnschrift', 10))
                        txt.place(x=15, y=70)
                        txt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        txt_in.insert(0, x[i]['text'])
                        txt_in.place(x=100, y=70)
                        borde_r = tk.Label(top, text="Border ", font=('Bahnschrift', 10))
                        borde_r.place(x=15, y=100)
                        border_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        border_in.insert(0, x[i]['border'])
                        border_in.place(x=100, y=100)
                        pad_x = tk.Label(top, text="pad x: ", font=('Bahnschrift', 10))
                        pad_x.place(x=15, y=130)
                        px_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        px_in.insert(0, x[i]['padx'])
                        px_in.place(x=100, y=130)
                        pad_y = tk.Label(top, text="pad y: ", font=('Bahnschrift', 10))
                        pad_y.place(x=15, y=160)
                        py_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        py_in.insert(0, x[i]['pady'])
                        py_in.place(x=100, y=160)
                        fnt = tk.Label(top, text="Font Size: ", font=('Bahnschrift', 10))
                        fnt.place(x=15, y=190)
                        fnt_in = tk.Entry(top, font=('Bahnschrift', 10), width=25)
                        fnt_in.insert(0, 10)
                        fnt_in.place(x=100, y=190)
                        fnt_fam = tk.Label(top, text="Font family: ", font=('Bahnschrift', 10))
                        fnt_fam.place(x=15, y=220)
                        fntf_in = ttk.Combobox(top,values=font_fams, text="Font Size: ", font=('Bahnschrift', 10))
                        fntf_in.insert(0, x[i]['font'])
                        fntf_in.place(x=100, y=220)
                        img_ = tk.Label(top, text="Image (if any): ", font=('Bahnschrift', 10))
                        img_.place(x=15, y=250)
                        x_res = tk.Label(top, text=" X res: ", font=('Bahnschrift', 10))
                        x_res.place(x=15, y=280)
                        x_res_in=tk.Entry(top, font=('Bahnschrift', 10), width=5)
                        x_res_in.place(x=100,y=280)
                        y_res = tk.Label(top, text=" Y res: ", font=('Bahnschrift', 10))
                        y_res.place(x=15, y=310)
                        y_res_in = tk.Entry(top, font=('Bahnschrift', 10), width=5)
                        y_res_in.place(x=100, y=310)
                        def on_upl():
                            try:
                                global images_list
                                f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
                                filename = filedialog.askopenfilename(filetypes=f_types)
                                print(filename)

                                images_list[f"{i}"] = ImageTk.PhotoImage(Image.open(filename).resize((int(x_res_in.get()), int(y_res_in.get()))))

                                x[i].configure(image=images_list[f"{i}"])
                            except Exception:
                                messagebox.showinfo("UI Builder","Enter Size of image")

                        img_in = tk.Button(top, command=on_upl, text="Select Image", width=15, font=('Bahnschrift', 10))
                        img_in.place(x=100, y=250)
                        def upds():
                            try:
                                bgn=bg_in.get()
                                fgn=fg_in.get()
                                bordern=border_in.get()
                                txtn=txt_in.get()
                                padxn=px_in.get()
                                padyn=py_in.get()
                                fntf=fntf_in.get()
                                x[i].deselect()
                                x[i]['bg']=bgn
                                x[i]['fg'] = fgn
                                x[i]['border'] = bordern
                                x[i]['text'] = txtn
                                x[i]['padx'] = padxn
                                x[i]['pady'] = padyn
                                x[i].configure(font=(str(fntf), int(fnt_in.get()),))
                            except Exception :
                                messagebox.showinfo("UI Builder","Re Check Your inputs and try again")
                            finally:
                                return 0
                        upd=tk.Button(top,text="Update",command=upds,bg="green", fg="white", font=('Bahnschrift', 13), border=0)
                        upd.place(x=120,y=340)
                        top.mainloop()
                        break
                    if a==0:
                        pass

        else:
            return 0
def on_delete_widget():
    a = list(x)

    for i in a:
        if x[i].widgetName == 'button':
            a = x[i]['activebackground']
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(activebackground=a)
            a = messagebox.askyesno("UI Builder", "Do you want to delete the flashing widget")
            if a==1:
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder",f"Deleted the  widget selected")
                break
            if a==0:
                pass
        if x[i].widgetName == 'radiobutton':
            a = x[i]['activebackground']
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(activebackground=a)
            a = messagebox.askyesno("UI Builder", "Do you want to delete the flashing widget")
            if a==1:
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder",f"Deleted the  widget selected")
                break
            if a==0:
                pass
        if x[i].widgetName == 'checkbutton':
            a = x[i]['activebackground']
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(activebackground=a)
            a = messagebox.askyesno("UI Builder", "Do you want to delete the flashing widget")
            if a==1:
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder",f"Deleted the  widget selected")
                break
            if a==0:
                pass
        if x[i].widgetName == 'checkbutton':
            a = x[i]['activebackground']
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(
                activebackground=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
            x[i].flash()
            time.sleep(0.5)
            x[i].configure(activebackground=a)
            a = messagebox.askyesno("UI Builder", "Do you want to delete the flashing widget")
            if a==1:
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder",f"Deleted the  widget selected")
                break
            if a==0:
                pass
Button_widget_upd=tk.Button(basicprop_frame,command=on_get_wid_props,text="Update Widget Properties",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_upd.place(x=35,y=50)

Button_widget_del=tk.Button(basicprop_frame,command=on_delete_widget,text="Delete widget",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_del.place(x=35,y=100)

Button_widget_add=tk.Button(basicprop_frame,command=on_delete_widget,text="Add widget",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_add.place(x=35,y=150)

def on_save_close():
    final_wids={}
    for i in list(va):
        def get_attributes(widget):
            pic={}
            widg = widget
            keys = widg.keys()
            pic['name']=widg.widgetName
            pic['place_x']=widg.winfo_x()
            pic['place_y'] = widg.winfo_y()
            pic['bg']=widg['bg']
            try:
                pic['fg']=widg['fg']
            except Exception:
                pass

            try:
                pic['cursor']=widg['cursor']
            except Exception:
                pass
            try:
                pic['bd']=int(widg['bd'])
            except Exception:
                pass
            try:
                pic['digits']=widg['digits']
            except Exception:
                pass
            try:
                pic['font']=widg['font']
            except Exception:
                pass
            try:
                pic['text']=widg['text']
            except Exception:
                pass
            try:
                pic['from']=widg['from']
            except Exception:
                pass
            try:
                pic['to']=widg['to']
            except Exception:
                pass
            try:
                pic['length']=widg['length']
            except Exception:
                pass
            try:
                pic['orient']=widg['orient']
            except Exception:
                pass
            try:
                pic['padx']=int(widg['padx'])
            except Exception:
                pass
            try:
                pic['pady']=int(widg['pady'])
            except Exception:
                pass
            try:
                pic['image']=images_list[f"x{i}"]
                pic['im_x']
                pic['im_y']
            except Exception:
                pass

            final_wids[i]=pic
        get_attributes(x[f"x{i}"])

    with open(root_path + '/widgets.json', 'w') as handle:
        json.dump(str(final_wids), handle)
    print(images_list)

Button_widget_save_close=tk.Button(basicprop_frame,command=on_save_close,text="Save and Close",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_save_close.place(x=35,y=200)

print(x)
root.mainloop()