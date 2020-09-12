from tkinter import *
from bs4 import BeautifulSoup
import requests
import webbrowser
new=2
top =Tk()


source = requests.get('http://webcrawler.ml').text
soup = BeautifulSoup(source, 'lxml')

thelabel = Label(top,text = 'Web Crawler')
thelabel.pack()
def ourfeatures():
    for sec_head in soup.find_all('div',class_='section-header'):

        head_line = sec_head.h2.text
        
        if head_line=='OUR Features':
            print(head_line)
            parag = sec_head.p.text
            print(parag)
            print()
            for download in soup.find_all('div',class_='media service-box wow fadeInRight'):
                head = download.h4.text
                print(head)
                paragraph = download.p.text
                print(paragraph)

            print()
def services():
    for sec_head in soup.find_all('div',class_='section-header'):

        head_line = sec_head.h2.text
        if head_line == 'Service':
            print(head_line)
            parag = sec_head.p.text
            print(parag)
            print()
            
            for media_heading in soup.find_all('div',class_='media service-box'):
                media = media_heading.h4.text
                print(media)
                paragrap = media_heading.p.text
                print(paragrap)
                print()
        

def about_us():
    for sec_head in soup.find_all('div',class_='section-header'):

        head_line = sec_head.h2.text
        if head_line == 'About Us':
            print(head_line)
            parag = sec_head.p.text
            print(parag)
            print()

            
            for web_crawler in soup.find_all('div',class_='col-sm-6 wow fadeInRight'):
                web = web_crawler.h3.text
                print(web)
                pragraph = web_crawler.p.text
                print(pragraph)
                print()

                
def our_team():
    for sec_head in soup.find_all('div',class_='section-header'):

        head_line = sec_head.h2.text
        if head_line == 'OUR TEAM':
            print(head_line)
            parag = sec_head.p.text
            print(parag)
            print()

            for about in soup.find_all('div',class_='team-info'):
                abou = about.h3.text
                print(abou)
                
                print()
def redirect():
    url = 'webcrawler.ml'
    webbrowser.open(url,new=new)



    
b=Button(top, text = "OUR Features",width=20,bg="black",fg='white',command=ourfeatures)
b.place(x=0,y=100)
b.pack(side=LEFT)

c=Button(top, text = "Services",width=20,bg="black",fg='white',command = services)
c.pack(side=LEFT)
d=Button(top, text = "About Us",width=20,bg="black",fg='white',command = about_us)
d.pack(side=LEFT)
e=Button(top, text = "OUR TEAM",width=20,bg="black",fg='white',command = our_team)
e.pack(side=LEFT)
f=Button(top, text = "Website link",width=20,bg="black",fg='white',command = redirect)
f.pack(side=TOP)


top.mainloop()
