import os
import tkinter as tk
from tkinter import messagebox, filedialog

'''
from tkinter import ttk
from twilio.rest import Client
from tkinter import scrolledtext
'''
from subprocess import call
import json
from PIL import Image, ImageTk

with open('main_details.json') as f:
   datas = json.load(f)

mainscreen=tk.Tk()
mainscreen.geometry('950x600')
mainscreen.resizable(0,0)
mainscreen.title("UI Builder")

'''menubar=tk.Menu(mainscreen)
menubar.add_command(label="File")
menubar.add_cascade(label="Hello")
mainscreen.config(menu=menubar)

'''

'''def on_forgot():

    account_sid = 'ACbf48d4618102147aeae7e093832b3b09'
    auth_token = '392ba4b50afbee434db5fe49213f05b6'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG0f8d40b437f48ed64000f04312539f3f',
        body='How Can You Forget Your Password',
        to='+919491956708'
    )

    print(message.sid)
'''

def on_logout():
    mainscreen.destroy()
    import Login

def changepass():


    def info():

        messagebox.showinfo("UI Builder","Password Updated!")

    top = tk.Toplevel(mainscreen)
    top.geometry("500x250")
    top.resizable(0,0)
    top.title("Change Password")
    top['bg']="#2b72cf"
    lab_UI = tk.Label(top,text="UI Builder", font=('Bahnschrift', 24), bg="#2b72cf", fg='white')
    lab_UI.place(x=330, y=5)

    old_lab=tk.Label(top,   text="Old password          :", font=('Bahnschrift', 14), bg="#2b72cf", fg='white')
    old_lab.place(x=30,y=80)
    new_lab = tk.Label(top, text="New password        :", font=('Bahnschrift', 14), bg="#2b72cf", fg='white')
    new_lab.place(x=30, y=120)
    ren_lab = tk.Label(top, text="Re-Enter password :", font=('Bahnschrift', 14), bg="#2b72cf", fg='white')
    ren_lab.place(x=30, y=160)
    old_in = tk.Entry(top, border=0, font=('Bahnschrift', 14,), fg='white', bg='#2a7ce8')
    old_in.place(x=240, y=82)
    new_in = tk.Entry(top, border=0, font=('Bahnschrift', 14,), fg='white', bg='#2a7ce8')
    new_in.place(x=240, y=122)
    ren_in = tk.Entry(top, border=0, font=('Bahnschrift', 14,), fg='white', bg='#2a7ce8')
    ren_in.place(x=240, y=162)

    upd_button=tk.Button(top,text="Update Password",border=0,command=info,font=('Bahnschrift', 14,), bg='white', fg='#2a7ce8')
    upd_button.place(x=200,y=205)

top_frame=tk.Frame(mainscreen,bg='#2b72cf',height=80,width=2000)
top_frame.place(x=0,y=0)

im_frame=tk.Frame(mainscreen,bg='white',height=1500,width=250)
im_frame.place(x=0,y=85)

image = Image.open("bg.jpg")
resize_image = image.resize((250, 500))
img = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(im_frame,image=img)
label1.image = img
label1.place(x=0,y=0)

left_frame=tk.Frame(mainscreen,bg='#B492F0',height=510,width=690)
left_frame.place(x=255,y=85)

def on_ce():
    call(["python", "code_editor.py"])
def on_up_s():
    call(["python","update_file.py"])
def on_run():
    call(["python","from_json.py"])
def on_download():
    def save_as():
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="from_json.py",
                defaultextension=".py",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css"),("Json Files","*.json")])
            with open('from_json.py','r') as k:
                b=k.read()
            with open(new_file, "w") as f:
                f.write(b)
        except Exception as e:
            print(e)
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile=datas['Root_path']+"/widgets.json",
                defaultextension=".json",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css"),("Json Files","*.json")])
            with open(datas['Root_path']+"widgets.json",'r') as k:
                b=k.read()
            with open(new_file, "w") as f:
                f.write(b)
        except Exception as e:
            print(e)
    save_as()


butt1=tk.Button(left_frame,text="Code Editor",command=on_ce,border=0,font=("Bahnchrift 12 bold"),width=67)
butt1.place(x=6,y=10)

lab_p1=tk.Label(left_frame,text="Project 1",font=('Bahnschrift',20),bg="#B492F0",fg='white')
lab_p1.place(x=75,y=100)

view_p1=tk.Button(left_frame,command=on_download,text="Download Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
view_p1.place(x=80,y=150)
run_p1=tk.Button(left_frame,command=on_run,text="Run Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
run_p1.place(x=80,y=175)
up_p1=tk.Button(left_frame,command=on_up_s,text="Update Structure",font=('Bahnschrift',10),bg="Green",fg='white',width=20,border=0)
up_p1.place(x=80,y=200)

lab_p2=tk.Label(left_frame,text="Project 2",font=('Bahnschrift',20),bg="#B492F0",fg='white')
lab_p2.place(x=275,y=100)
run_p2=tk.Button(left_frame,command=on_run,text="Run Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
run_p2.place(x=280,y=175)
view_p2=tk.Button(left_frame,command=on_download,text="Download Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
view_p2.place(x=280,y=150)

up_p2=tk.Button(left_frame,command=on_up_s,text="Update Structure",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
up_p2.place(x=280,y=200)

lab_p3=tk.Label(left_frame,text="Project 3",font=('Bahnschrift',20),bg="#B492F0",fg='white')
lab_p3.place(x=475,y=100)
up_p3=tk.Button(left_frame,command=on_up_s,text="Update Structure",font=('Bahnschrift',10),bg="Green",fg='white',width=20,border=0)
up_p3.place(x=480,y=200)
view_p2=tk.Button(left_frame,command=on_download,text="Download Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
view_p2.place(x=480,y=150)
run_p3=tk.Button(left_frame,text="Run Code",command=on_run,font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
run_p3.place(x=480,y=175)
lab_p4=tk.Label(left_frame,text="Project 4",font=('Bahnschrift',20),bg="#B492F0",fg='white')
lab_p4.place(x=75,y=300)

view_p4=tk.Button(left_frame,command=on_download,text="Download Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
view_p4.place(x=80,y=350)
up_p4=tk.Button(left_frame,command=on_up_s,text="Update Structure",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
up_p4.place(x=80,y=400)
run_p4=tk.Button(left_frame,text="Run Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
run_p4.place(x=80,y=375)

lab_p5=tk.Label(left_frame,text="Project 5",font=('Bahnschrift',20),bg="#B492F0",fg='white')
lab_p5.place(x=275,y=300)
run_p5=tk.Button(left_frame,text="Run Code",command=on_run,font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
run_p5.place(x=280,y=375)
view_p5=tk.Button(left_frame,command=on_download,text="Download Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
view_p5.place(x=280,y=350)
up_p5=tk.Button(left_frame,command=on_up_s,text="Update Structure",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
up_p5.place(x=280,y=400)

lab_p6=tk.Label(left_frame,text="Project 6",font=('Bahnschrift',20),bg="#B492F0",fg='white')
lab_p6.place(x=475,y=300)
up_p6=tk.Button(left_frame,command=on_up_s,text="Update Structure",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
up_p6.place(x=480,y=400)
run_p6=tk.Button(left_frame,command=on_run,text="Run Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
run_p6.place(x=480,y=375)
view_p6=tk.Button(left_frame,command=on_download,text="Download Code",font=('Bahnschrift',10),bg="Green",fg='white',border=0,width=20)
view_p6.place(x=480,y=350)

lab_UI=tk.Label(text="UI Builder",font=('Bahnschrift',24),bg="#2b72cf",fg='white')
lab_UI.place(x=780,y=20)

lab_Uname=tk.Label(text=f"Welcome, {datas['User']}!",font=('Bahnschrift',20),bg="#2b72cf",fg='white')
lab_Uname.place(x=20,y=5)

logout=tk.Button(mainscreen,text="Logout", font=('Bahnschrift',12),command=on_logout,border=0,bg="#2b72cf",fg='white')
logout.place(x=20,y=45)

changepass=tk.Button(mainscreen,text="Change Password",command=changepass, font=('Bahnschrift',12),border=0,bg="#2b72cf",fg='white')
changepass.place(x=100,y=45)

mainscreen.mainloop()