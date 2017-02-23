"""from Logs import *
from HTMLScrapping import *


# Main function that takes input of user
def user():
    user_name = str(input('ENTER YOUR NAME : '))
    query = str(input('ENTER YOUR QUERY TO BE SEARCHED ON YOUTUBE : '))
    create_dir()
    data(user_name, query)
    link = urlifystring(query)
    html_parser(link)

user()"""

__author__ = 'Harsh'
from tkinter import *
from HTMLScrapping import *
from Logs import *

a=["1"]
def search(enter=1):
    temp=urlifystring(text.get())
    scrapping(temp)
def next():
   count=a[0]
   msg=browser_open(int(count))
   if msg==1:
       lb4=Label(window,text="No More Links").place(x=80,y=70)
   a[0]=str(int(count)+1)
window=Tk()
window.geometry("300x100")
window.title("Youtube Bot")
lbl=Label(window,text='Search Here',font=("Charlemagne Std",14)).place(x=40,y=6)

text=Entry(window,bd=4,width=35)
text.place(x=40,y=40)
text.focus()
text.bind("<Return>",search)

b1=Button(window,text="Search",command=search,bd=3,font=("Charlemagne Std",10),bg="#99AABB").place(x=140,y=70)
b2=Button(window,text="Next",command=next,bd=3,font=("Charlemagne Std",10),bg="#99AABB").place(x=230,y=69)
#print(str(count)+"2")
window.mainloop()



