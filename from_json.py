import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk,ImageOps
import ast
import json
with open('main_details.json') as f:
   datas = json.load(f)
with open(datas['Root_path']+"/widgets.json", "r") as f:
   a=json.load(f)
try:
   with open(datas['Root_path']+"/images.json", "r") as f:
      imgs=json.load(f)
   imgs=eval(imgs)
except FileNotFoundError:
   pass
va=eval(a)
root=datas['Root_path']
new_path=root+'/basic_details.json'
with open(new_path) as f:
   data_basic = json.load(f)
try:
   data_basic=eval(data_basic)
except TypeError:
   pass
print(data_basic)
screen_render=tk.Tk()
screen_render['height']=int(data_basic['height'])
screen_render['width']=int(data_basic['width'])
screen_render.resizable(0,0)
screen_render['bg']=data_basic['bg']

b={}
for i in list(va.keys()):

   a=va[i]
   if a['name']=='scale':
      b[i]=tk.Scale()
   elif a['name']=='button':
      b[i]=tk.Button()
   elif a['name'] == 'entry':
      b[i] = tk.Entry()
   elif a['name'] == 'radiobutton':
      b[i] = tk.Radiobutton()
   elif a['name'] == 'checkbutton':
      b[i] = tk.Button()
   elif a['name'] == 'label':
      b[i] = tk.Label()
   b[i].place(x=a['place_x'], y=a['place_y'])
   for j in range(3, len(a.keys())):
      b[i][list(a.keys())[j]] = list(a.values())[j]


for i in imgs.keys():
   try:
       imgb = Image.open("sample.jpg")
       img_resized = imgb.resize((250, 250))
       imgb = ImageTk.PhotoImage(img_resized)
       c=b[i]
       print(c.configure(image=ImageTk.PhotoImage(Image.open(imgs[i]['path']).resize((int(imgs[i]['width'])), int(imgs[i]['height'])))))
   except KeyError:
      pass
print(b)
screen_render.mainloop()

