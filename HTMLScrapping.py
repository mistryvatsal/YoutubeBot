__author__ = 'Harsh'
import webbrowser
import requests
import re
lista=[]
def scrapping(link):
    global lista
    lista=re.findall('href="(/watch.*?)"',requests.get(link, "html.parser").text)
    webbrowser.open("https://www.youtube.com" + lista[0])
def browser_open(count):
    try: webbrowser.open("https://www.youtube.com"+lista[count])
    except IndexError: return 1

