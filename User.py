__author__ = 'Harsh'
from tkinter import *
from HTMLScrapping import *
import _thread
from Logs import *

count=1
def search(enter=1):
    temp=urlifystring(text.get())
    _thread.start_new_thread(scrapping, (temp,))
    #scrapping(temp)
def next():
    global count
    msg=browser_open(int(count))
    if msg==1:
       lb4=Label(window,text="No More Links").place(x=80,y=70)
    count+=1
window=Tk()
window.geometry("300x100")
window.title("Youtube Bot")
window.call('wm', 'attributes', '.', '-topmost', '1')
lbl=Label(window,text='Search Here',font=("Charlemagne Std",14)).place(x=40,y=6)

text=Entry(window,bd=4,width=35)
text.place(x=40,y=40)
text.focus()
text.bind("<Return>",search)

b1=Button(window,text="Search",command=search,bd=3,font=("Charlemagne Std",10),bg="#99AABB").place(x=140,y=70)
b2=Button(window,text="Next",command=next,bd=3,font=("Charlemagne Std",10),bg="#99AABB").place(x=230,y=69)

window.mainloop()



