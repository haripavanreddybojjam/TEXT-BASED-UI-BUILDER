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
    print(va)
    try:
        va=eval(va)
    except TypeError:
        pass
except FileNotFoundError:
    va={"bg": "white", "width": 750, "height": 400, "title": ""}
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
images_json={}
allow_dd=0
x={}

root=tk.Tk()
root.geometry('1080x720')
root.minsize(1080,720)
root.title("UI Builder")

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

ele=[]

def on_create_atts():
    global ele
    for i in range(len(ele)):
        if ele[i].lower() == "button":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Button()
            x[a] = tk.Button(samp_frame, text="Sample Text Here!")
        if ele[i].lower() == "text_entry":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Entry(samp_frame, text="Sample Text Here!", width=10)
            x[a] = tk.Entry(samp_frame, text="Sample Text Here!", width=10)
        if ele[i].lower() == "radiobutton":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Radiobutton(samp_frame)
            x[a] = tk.Radiobutton(samp_frame)
        if ele[i].lower() == "check_button":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Checkbutton(samp_frame)
            x[a] = tk.Checkbutton(samp_frame)
        if ele[i].lower() == "label":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Label(samp_frame)
            x[a] = tk.Label(samp_frame, text="sample text")
        if ele[i].lower() == "scale":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Scale(samp_frame)
            x[a] = tk.Scale(samp_frame)

        if ele[i].lower() == "scrollbar":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Scrollbar(samp_frame)
            x[a] = tk.Scrollbar(samp_frame)

        if ele[i].lower() == "combobox":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = ttk.Combobox(samp_frame)
            x[a] = ttk.Combobox(samp_frame)

        if ele[i].lower() == "spinbox":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Spinbox(samp_frame)
            x[a] = tk.Spinbox(samp_frame)
        if ele[i].lower() == "image":
            a = f'x{random.randint(0, 999999)}'
            globals()[a] = tk.Button(samp_frame, border=0)
            x[a] = tk.Button(samp_frame, border=0)
            imgb = Image.open("sample.jpg")
            img_resized = imgb.resize((250, 250))
            imgb = ImageTk.PhotoImage(img_resized)
            x[a].configure(image=imgb)
    for i in range(len(list(x.keys()))):
        x[list(x.keys())[i]].place(x=i * 20 + 20, y=i * 20 + 20)
    ele.clear()
on_create_atts()
global_i=0

def on_enable():
    global allow_dd

    main_button.configure(text="Disable Drag Drop",bg="Green",fg="white",font=('Bahnschrift', 13, 'bold'), border=0)
    allow_dd = 1
    for i in list(x.keys()):
        x[f'{i}'].bind("<Button-1>", drag_start)
        x[f'{i}'].bind("<B1-Motion>", drag_motion)
        print(x[f'{i}'].winfo_x())
        print(x[f'{i}'].winfo_y())
        print(f"x{i}===========================================")

def on_disable():
    global allow_dd

    main_button.configure(text="Enable Drag Drop", bg="Red", fg="white", font=('Bahnschrift', 13, 'bold'), border=0)
    allow_dd = 0
    for i in list(x.keys()):
        x[f'{i}'].unbind("<Button-1>")
        x[f'{i}'].unbind("<B1-Motion>")
        print(x[f'{i}'].winfo_x())
        print(x[f'{i}'].winfo_y())
        print(f"x{i}===========================================")

def on_click_drag_drop():
    global allow_dd
    if allow_dd==1:
        on_disable()
    else:
        on_enable()

def on_delete_widget():
    a = list(x.keys())
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
        if x[i].widgetName == 'check_button':
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
        if x[i].widgetName == 'label':
            content = x[i]['bg']
            x[i].configure(bg="red")
            time.sleep(1)
            a = messagebox.askyesno("UI Builder", "Do you want to Delete the Red Text  ?")

            if a == 1:
                x[i].configure(bg=content)
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder", f"Deleted the  widget selected")
                break
            if a==0:
                x[i].configure(bg=content)
        if x[i].widgetName == 'text_entry':
            content = x[i]['bg']
            x[i].configure(bg="red")
            time.sleep(1)
            a = messagebox.askyesno("UI Builder", "Do you want to Delete the Red Text  ?")

            if a == 1:
                x[i].configure(bg=content)
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder", f"Deleted the  widget selected")
                break
            if a==0:
                x[i].configure(bg=content)
        if x[i].widgetName == 'scale':
            content = x[i]['bg']
            x[i].configure(bg="red")
            time.sleep(1)
            a = messagebox.askyesno("UI Builder", "Do you want to Delete the Red Text  ?")

            if a == 1:
                x[i].configure(bg=content)
                x[i].destroy()
                del x[f"{i}"]
                print(x)
                messagebox.showinfo("UI Builder", f"Deleted the  widget selected")
                break
            if a==0:
                x[i].configure(bg=content)

update_frame=tk.Frame(root,bg='#7ab541',height=800,width=278)
update_frame.place(x=0,y=81)

text_frame=tk.Frame(update_frame,bg='#10535b',width=278,height=244)
text_frame.place(x=0,y=0)

upload_im=tk.Label(text_frame,text="Upload Requirements Text Below",bg='#10535b',fg='white',font=('Bahnschrift',13))
upload_im.place(x=10,y=7)


in_text=tk.Text(text_frame, width=32, height=8)
in_text.place(x=10,y=70)
datas={}
def on_gen():
    global ele,datas
    print(ele)
    ele.clear()
    print(ele)
    given_NLP_text=in_text.get("1.0","end-1c")

    import spacy
    import json

    nlp_ner = spacy.load("model-best")
    doc = nlp_ner(given_NLP_text)
    with open('main_details.json') as f:
        datas = json.load(f)
    root_path = datas['Root_path']
    for_basic = {}
    others = {}
    try:
        print(doc.ents)
        for i in doc.ents:
            if i.label_ == "BG":
                for_basic['bg'] = str(i)
            elif i.label_ == "SCREEN_RESOL":
                a = str(i).split('x')
                for_basic['width'] = int(a[0])
                for_basic['height'] = int(a[1])
            else:
                others[i.label_] = i
        with open(root_path + '/basic_details.json', 'w') as f:
            json.dump(str(for_basic), f)
            print(for_basic)
        with open(root_path + '/wid_from.json', 'w') as f:
            print(others)
            json.dump(str(others), f)
    except UserWarning:
        print("NO INPUT")

    print(given_NLP_text)
    in_text.delete("1.0","end")

    try:
        with open(root_path+'/basic_details.json') as f:
            datas = json.load(f)

        datas = eval(datas)
        samp_frame['height']=datas['height']
        samp_frame['width']=datas['width']
        samp_frame['bg']=datas['bg']
    except FileNotFoundError:
        messagebox.showinfo("UI Builder","Something went wrong, Retry")
    try:
        with open(root_path+'/wid_from.json') as f:
            a=json.load(f)

        a=eval(a)
        for i in a.keys():
            for j in range(int(a[i])):
                ele.append(i)
        print(ele)
        on_create_atts()
    except FileNotFoundError:
        pass


upload_button=tk.Button(text_frame,command=on_gen,text="Generate",border=0,width=10)
upload_button.place(x=100,y=40)

allow_frame=tk.Frame(update_frame,bg='#10535b',width=278,height=45)
allow_frame.place(x=0,y=250)

main_button=tk.Button(allow_frame,text="Enable Drag and Drop",command=on_click_drag_drop,width=25,bg="Red", fg="white", font=('Bahnschrift', 13, 'bold'), border=0)
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
            a=list(x.keys())

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
                                images_json[i]={'path':filename,'width':int(x_res_in.get()),'height':int(y_res_in.get())}




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
                if x[i].widgetName=='text_entry':
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
                if x[i].widgetName=='check_button':
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
Button_widget_upd=tk.Button(basicprop_frame,command=on_get_wid_props,text="Update Widget Properties",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_upd.place(x=35,y=50)

Button_widget_del=tk.Button(basicprop_frame,command=on_delete_widget,text="Delete widget",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_del.place(x=35,y=100)
def on_add_widget():
    a=tk.Toplevel()
    a.geometry('200x150')
    a.resizable(0,0)
    l1=tk.Label(a,text="Enter a widget name below",font=('Bahnschrift', 10))
    l1.place(x=10,y=10)
    b1=tk.Entry(a,width=15,font=('Bahnschrift', 10))
    b1.place(x=40,y=35)
    def add_wid():
        global ele
        ele.clear()
        ele.append(str(b1.get()).lower())
        on_create_atts()
    tk.Button(a,text="Add Widget",width=15,font=('Bahnschrift', 10),command=add_wid).place(x=40,y=80)
    a.mainloop()
Button_widget_add=tk.Button(basicprop_frame,command=on_add_widget,text="Add widget",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_add.place(x=35,y=150)
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
def on_save_close():
    print(images_json)
    final_wids={}
    for i in list(x.keys()):
        def get_attributes(widget):
            pic={}
            widg = widget
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
            except Exception:
                pass

            final_wids[i]=pic
        get_attributes(x[i])

    with open(root_path + '/widgets.json', 'w') as handle:
        json.dump(str(final_wids), handle)
    with open(root_path + '/images.json', 'w') as handle:
        json.dump(str(images_json), handle)
    print(images_list)
    print(final_wids)

Button_widget_save_close=tk.Button(basicprop_frame,command=on_save_close,text="Save and Close",bg="#AF0334", fg="white", font=('Bahnschrift', 13, 'bold'), border=0,width=22)
Button_widget_save_close.place(x=35,y=200)

root.mainloop()