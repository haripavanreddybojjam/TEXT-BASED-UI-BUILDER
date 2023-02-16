import smtplib
import tkinter as tk
from PIL import ImageTk, Image
from subprocess import call
from threading import Thread
from tkinter import messagebox
from pymongo import MongoClient
import os
import json


client = MongoClient('localhost', 27017)

db = client['mydb']

collection = db['uibuilderdata']

login_page=tk.Tk()
login_page.geometry('750x500')
login_page.resizable(False,False)
login_page.configure(bg='white')
login_page.title("UI Builder")
'''
img0 = ImageTk.PhotoImage(Image.open("D:\Project\logo.png"))
logo_lab = tk.Label(image = img0)
logo_lab.place(x=570,y=-3)'''


def on_forgot():
    a= usernamein.get()
    if len(a)==0:
        messagebox.showerror("UI BUILDER","Enter your Username")
        return 0
    if collection.find({"username":a}):

        from twilio.rest import Client

        account_sid = 'ACbf48d4618102147aeae7e093832b3b09'
        auth_token = '392ba4b50afbee434db5fe49213f05b6'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid='MG0f8d40b437f48ed64000f04312539f3f',
            body='Your password is ******',
            to='+917989006406'
        )
    else:
        messagebox.showerror("UI BUILDER","Username not found")

    print(message.sid)


def on_login():
    if collection.find_one({"$and": [{"username":usernamein.get()},{"password":passwordin.get()}]}):
        x=collection.find_one({"username":usernamein.get()})
        new_json = {"User": usernamein.get(),"Root_path" : str(x['path'])}
        with open("main_details.json", "w") as outfile:
            json.dump(new_json, outfile)
        login_page.destroy()
        import main_file


    else:
        messagebox.showwarning("UI BUILDER","Please Check your username and password")

def on_register():
    os.system("python register.py")



tc=tk.Label(text="Amrita Vishwa Vidyapeetham",font=('Bahnschrift',10),fg='gray',bg="white")
tc.place(x=560,y=475)
img = ImageTk.PhotoImage(Image.open("login.jpg"))
imgleft_lab = tk.Label(image = img)
imgleft_lab.place(x=-3,y=-3)

Welcome=tk.Label(text="Welcome to UI Builder",bg='white',font=('Bahnschrift',24),fg='#060C13')
Welcome.place(x=330,y=60)

Signintxt=tk.Label(text="Login/Register",bg='white',font=('Bahnschrift',18),fg='#0D6281')
Signintxt.place(x=400,y=145)

Usernametext=tk.Label(text="Username    :",bg='white',font=('Bahnschrift',13,),fg='#7A7A7A')
Usernametext.place(x=300,y=210)

usernamein=tk.Entry(login_page,border=0,font=('Bahnschrift',13,),fg='black',bg='#F6F6F6')
usernamein.place(x=420,y=213)

passwordtext=tk.Label(text="Password    :",bg='white',font=('Bahnschrift',13,),fg='#7A7A7A')
passwordtext.place(x=300,y=250)

passwordin=tk.Entry(login_page,show='*',border=0,font=('Bahnschrift',13,),fg='black',bg='#F6F6F6')
passwordin.place(x=420,y=253)

login_button = tk.Button(login_page, text="Log in",width=14, font=('Bahnschrift', 13,'bold'),command=on_login,border=0, bg='#086587',fg='#FCFCFC')
login_button.place(x=420, y=320)

fpwd_button = tk.Button(login_page, text="Forgot Password",command=on_forgot,font=('Bahnschrift', 12,'underline'),border=0, fg='black',bg='#FCFCFC')
fpwd_button.place(x=420, y=360)

noaccounttext=tk.Label(text="Don't Have an account?",bg='white',font=('Bahnschrift',13,),fg='#7A7A7A')
noaccounttext.place(x=300,y=420)

register_button = tk.Button(login_page, text="New User, Register Here!", font=('Bahnschrift', 13,'bold','underline'),command=on_register,border=0, fg='#332D2D',bg='#FCFCFC')
register_button.place(x=500, y=417)

login_page.mainloop()

