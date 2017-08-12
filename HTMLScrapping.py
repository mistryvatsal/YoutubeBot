__author__ = 'Harsh'
import webbrowser
import bs4
import requests
import urllib.request
import _thread

lista=[]
def first_open(temp):
    webbrowser.open("https://www.youtube.com"+temp)

def add_list(temp):
    lista.append(temp)

def scrapping(link):
    del lista[0:len(lista)]
    print("in")
    #l=requests.get("http://"+link)
    #l=l.text   we can use this in place of urlopen to get the requests of urls and converting to text to use it for beautifulsoup
    a=urllib.request.urlopen(link)
    soup=bs4.BeautifulSoup(a,"lxml")
    flag=0
    for i in soup.find_all(class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "):
        temp=str(i.get("href"))
        if(flag==0):
            _thread.start_new_thread(first_open,(temp,))
            flag=1
        _thread.start_new_thread(add_list,(temp,))
        #lista.append(temp)
    print("out")

def browser_open(count):
    try:
        webbrowser.open("https://www.youtube.com"+lista[count])
    except IndexError:
        return 1




#another method to find for first link directly
#i=soup.find(class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link")
#print(i.get("href"))

#webbrowser.open("https://www.youtube.com"+i.get("href"))
