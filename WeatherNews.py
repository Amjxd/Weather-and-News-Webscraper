from tkinter import *
from PIL import ImageTk, Image
import requests
import bs4



#WEATHER

root = Tk()
root.configure(bg = '#36373b')
root.geometry('330x100')
root.title('Daily News / Weather')

weather_lbl = Label(root,text = "Show Today's Weather →",fg='white',bg = '#36373b',font = ('arial',16,'bold'))
weather_lbl.grid(column=0,row=0,columnspan=2)

def check_weather():
    city = clicked.get()
    if city == 'Mississauga':
        name = '24'
    elif city == 'Toronto':
        name = '143'
    elif city == 'Brampton':
        name = '4'
    elif city == 'Oakville':
        name = '79'
    elif city == 'Hamilton':
        name = '24'
    elif city == 'Barrie':
        name = '151'
    elif city == 'Kingston':
        name = '69'
    else:
        name = '64'
    req = requests.get(f'https://weather.gc.ca/city/pages/on-{name}_metric_e.html')
    soup = bs4.BeautifulSoup(req.text,'lxml')
    top = Toplevel()
    top.title(f'{city} Weather')
    top.configure(bg = '#36373b')
    top.geometry('320x130')

    #Celcius
    t=(soup.select('.wxo-metric-hide')[2]).text
    lst = []
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for i in t:
        for q in nums:
            if q in i:
                lst.append(i)
    lst = ''.join(lst)
    lst = f"{lst}°C ~ {city}"
    celcius = Label(top,text = lst, font = ('arial',25,'bold'),fg = 'yellow',bg = '#36373b')
    celcius.grid(column=0,row=0,columnspan=3,pady=8)

    #Pressure
    t=(soup.select('.wxo-metric-hide')[4]).text
    pressure1 = Label(top,text = f'Pressure: {t}', font = ('arial',12),fg = 'white',bg = '#36373b')
    pressure1.grid(column=0,row=1)
    
    #Temp
    t=(soup.select('.wxo-metric-hide')[5]).text
    temp1 = Label(top,text = f'Temprature: {t}', font = ('arial',12),fg = 'white',bg = '#36373b')
    temp1.grid(column=0,row=2)
    
    #Dew point
    t=(soup.select('.wxo-metric-hide')[6]).text
    dew1 = Label(top,text = f'Dew Point: {t}', font = ('arial',12),fg = 'white',bg = '#36373b')
    dew1.grid(column=1,row=1)

    #wind
    t=(soup.select('.wxo-metric-hide')[7]).text
    wind1 = Label(top,text = f'Wind: {t}', font = ('arial',12),fg = 'white',bg = '#36373b')
    wind1.grid(column=1,row=2)

    #Humidex
    t=(soup.select('.wxo-metric-hide')[8]).text
    humi = Label(top,text = f'Humidex: {t}', font = ('arial',12),fg = 'white',bg = '#36373b')
    humi.grid(column=2,row=1)

    #Visibility
    t=(soup.select('.wxo-metric-hide')[9]).text
    humi = Label(top,text = f'Visibility: {t}', font = ('arial',12),fg = 'white',bg = '#36373b')
    humi.grid(column=2,row=2)

def weather():
    global clicked
    city = Label(root,text = 'City:',fg='white',bg = '#36373b',font = ('arial',16,'bold'))
    city.grid(column=0,row=1)
    cities = ["Toronto",'Mississauga','Brampton','Oakville','Hamilton','Barrie','Kingston','Vaughan']
    clicked = StringVar()
    clicked.set(cities[1])
    drop = OptionMenu(root,clicked,*cities)
    drop.config(bg='#36373b') #changing the color of the drop down menu background
    drop.grid(column=1,row=1)
    submit = Button(root, text = 'Submit', width = 8, highlightbackground = '#36373b',command = check_weather)
    submit.grid(column=3,row=1,padx=2)

weather_but = Button(root, text = 'WEATHER', width = 8, highlightbackground = '#36373b',command = weather)
weather_but.grid(column=3,row=0,padx=2)

#NEWS
def get_news():
    req = requests.get('https://globalnews.ca/')
    soup = bs4.BeautifulSoup(req.text,'lxml')
    top = Toplevel()
    top.title('Global News')
    top.configure(bg = '#36373b')
    top.geometry('780x506')
    path = "header.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img #fixes blank image
    panel.grid(column=0,row=0)

    #HEADLINE
    t=(soup.select('.c-posts__inner')[9]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    framehead = LabelFrame(top,padx = 1,pady = 15)
    framehead.grid(row=1,column=0)
    headline = t[1]
    headline = Label(framehead,text = f'HEADLINE: {headline}', font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    headline.grid(column=0,row=1)

    #News 1
    t=(soup.select('.c-posts__inner')[10]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'1 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=2,pady=10)

    #News 2
    t=(soup.select('.c-posts__inner')[11]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'2 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=3)


    #News 3
    t=(soup.select('.c-posts__inner')[12]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'3 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=4,pady=10)

    #News 4
    t=(soup.select('.c-posts__inner')[13]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'4 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=5)

    #News 5
    t=(soup.select('.c-posts__inner')[14]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'5 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=6,pady=10)

    #News 6
    t=(soup.select('.c-posts__inner')[15]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'6 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=7)

    #News 7
    t=(soup.select('.c-posts__inner')[16]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'7 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=8,pady=10)

    #News 8
    t=(soup.select('.c-posts__inner')[17]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'8 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=9)

    #News 9
    t=(soup.select('.c-posts__inner')[18]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'9 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=10,pady=10)

    #News 10
    t=(soup.select('.c-posts__inner')[17]).text
    t= t.split('\n')
    while '' in t:
        t.remove('')
    newsone = Label(top,text=f'10 - {t[0]}',font = ('arial',16,'bold'),fg = 'white',bg = '#36373b')
    newsone.grid(column=0,row=11)
    
    
news_lbl = Label(root,text = "Show Today's News →",fg='white',bg = '#36373b',font = ('arial',16,'bold'))
news_lbl.grid(column=0,row=2,columnspan=2)

news_but = Button(root, text = 'NEWS', width = 8, highlightbackground = '#36373b',command = get_news)
news_but.grid(column=3,row=2,padx=2)
root.mainloop()
