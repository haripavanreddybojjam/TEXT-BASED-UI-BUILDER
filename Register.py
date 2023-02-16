import tkinter as tk
from PIL import ImageTk, Image
from subprocess import call
from threading import Thread
from pymongo import MongoClient
from tkinter import messagebox
import json
import os


client = MongoClient('localhost', 27017)
db = client['mydb']

collection = db['uibuilderdata']


show_pass=0
def on_showhide():
    global show_pass
    if show_pass==1:
        show_pass=0
        hide_pwd()
    else:
        show_pass=1
        show_pwd()

def show_pwd():
    passwordin.configure(show='')
    showpassbuton.configure(text="Hide")

def hide_pwd():
    passwordin.configure(show="*")
    showpassbuton.configure(text="Show")

def take_in():
    username = usernamein.get()
    password = passwordin.get()
    mobile = repasswordin.get()
    mail = mail_in.get()
    acc = checkin.get()
    checkinp(username, password, mobile, mail, acc)


def checkinp(username, password, mobile, mail, acc):
    counts = 0
    if collection.find_one({"username": username}):
        messagebox.showerror("UI Builder", "Username already Exists!")

    else:
        counts += 1

        if len(password) < 8:
            messagebox.showerror("UI Builder", "Choose a longer password")
        else:
            counts+=1

            if len(mobile)==10 :
                counts+=1
            counts+=acc
            if acc==0:
                messagebox.showwarning("UI Builder","Select all options before proceeding ")
    if counts==4:
        messagebox.showinfo("UI Builder","Welcome to the community "+username+", Reopen the application to start using it!")
        directory = username
        parent_dir = "Documents/UIBUilder"
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path, exist_ok=True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)

        user_data = [{username: f"Documents/UIBUilder/{username}"}]
        list_users = [{"username": username, "password": password, "mobile": str(mobile), "Mail": mail, "path":f"Documents/UIBUilder/{username}"}]
        print(list_users)
        collection.insert_many(list_users)

        with open('new_file.json', 'w') as f:
            json.dump(user_data, f)

        quit()
    else:
        messagebox.showerror("UI Builder", "Fill all the Details")


def registerInfo():
    messagebox.showinfo("UI Builder", "Welcome to UI Builder Family!")


register_page = tk.Tk()
register_page.geometry('750x500')
register_page.resizable(False, False)
register_page.configure(bg='white')
register_page.title("UI Builder")

img = ImageTk.PhotoImage(Image.open("login.jpg"))
imgleft_lab = tk.Label(image=img)
imgleft_lab.place(x=-3, y=-3)

Welcome = tk.Label(text="Welcome to UI Builder", bg='white', font=('Bahnschrift', 24), fg='#060C13')
Welcome.place(x=330, y=60)
Registertxt = tk.Label(text="Register", bg='white', font=('Bahnschrift', 18), fg='#0D6281')
Registertxt.place(x=450, y=145)

Usernametext = tk.Label(text="Username    :", bg='white', font=('Bahnschrift', 13,), fg='#7A7A7A')
Usernametext.place(x=330, y=210)

usernamein = tk.Entry(register_page, border=0, font=('Bahnschrift', 13,), fg='black', bg='#F6F6F6')
usernamein.place(x=450, y=213)

passwordtext = tk.Label(text="Password    :", bg='white', font=('Bahnschrift', 13,), fg='#7A7A7A')
passwordtext.place(x=330, y=250)

passwordin = tk.Entry(register_page,show="*", border=0, font=('Bahnschrift', 13,), fg='black', bg='#F6F6F6')
passwordin.place(x=450, y=253)

showpassbuton=tk.Button(register_page,command=on_showhide,text="Show",border=0,bg="white",fg="gray",font=("Bahnschrift",10))
showpassbuton.place(x=650,y=253)

mobile = tk.Label(text="Contact     :", bg='white', font=('Bahnschrift', 13,), fg='#7A7A7A')
mobile.place(x=330, y=290)

repasswordin = tk.Entry(register_page, border=0, font=('Bahnschrift', 13,), fg='black', bg='#F6F6F6')
repasswordin.place(x=450, y=293)

mail_text = tk.Label(text="Mail ID         :", bg='white', font=('Bahnschrift', 13,), fg='#7A7A7A')
mail_text.place(x=330, y=330)

mail_in = tk.Entry(register_page, border=0, font=('Bahnschrift', 13,), fg='black', bg='#F6F6F6')
mail_in.place(x=450, y=330)

checkin = tk.IntVar()

accept_terms = tk.Checkbutton(register_page, variable=checkin, bg='white', fg='Green')
accept_terms.place(x=295, y=380)
accept_terms_text = tk.Label(text="By clicking you agree to the terms and conditions", font=('Bahnschrift', 12),
                             fg='gray', bg='white')

accept_terms_text.place(x=330, y=380)
login_button = tk.Button(register_page, text="Register", command=take_in, font=('Bahnschrift', 13, 'bold'), border=0,
                         bg='#086587', fg='#FCFCFC')
login_button.place(x=470, y=420)

tc = tk.Label(text="Amrita Vishwa Vidyapeetham", font=('Bahnschrift', 10), fg='gray', bg="white")
tc.place(x=560, y=475)
register_page.mainloop()
