import requests
from bs4 import BeautifulSoup
from theTime import *

page = requests.get("https://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=2542")
html = page.content
soup = BeautifulSoup(html,"html.parser")

t10 = time10("FirstRing")
t8 = time8("SecondRing")
t5 = time5("ThirdRing")
t2 = time2("FinalRing")

def ring1():
    if t10 in str (html):
        return True
def ring2():
    if t8 in str (html):
        return True
def ring3():
    if t5 in str (html):
        return True
def ring4():
    if t2 in str (html):
        return True


