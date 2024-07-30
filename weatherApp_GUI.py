from tabnanny import check
from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from time import strftime
from datetime import datetime

w = Tk()
w.geometry('800x400')
w.title("Weather App")
w.resizable(0, 0)

def weather_data(query):
    try:
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&units=metric&appid=f417c73c688486dca8ce7d002d66d32a')
        res.raise_for_status()  # Raise HTTPError for bad responses
        return res.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to get data: {e}")
        return None

Frame(w, width=800, height=50, bg='#353535').place(x=0, y=0)

# Search bar
imgSearch = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/search.PNG"))

def on_entry(e):
    el.delete(0, 'end')

def on_leave(e):
    if el.get() == '':
        el.insert(0, 'Search City')

el = Entry(w, width=21, fg='white', bg='#353535', border=0)
el.config(font={'Calibry', 12})
el.bind("<FocusIn>", on_entry)
el.bind("<FocusOut>", on_leave)
el.insert(0, 'Search City')
el.place(x=620, y=15)

# Date Format
a = datetime.today().strftime('%B')
b = (a.upper())
q = datetime.now().month
now = datetime.now()
c = now.strftime('%B')
month = c[0:3]

today = datetime.today()
date = today.strftime("%d")

def label(a):
    Frame(width=500, height=50, bg="#353535").place(x=0, y=0)

    l1 = Label(w, text=str(a), bg="#353535", fg="white")
    l1.config(font=("Calibry", 18))
    l1.place(x=20, y=8)

    city = a
    query = 'q=' + city
    w_data = weather_data(query)
    if not w_data:
        return

    result = w_data

    try:
        check = '{}'.format(result['main']['temp'])
    except KeyError:
        messagebox.showinfo("", "City not found")
        return

    c = int(float(check))
    description = "{}".format(result['weather'][0]['description'])
    weather = "{}".format(result['weather'][0]['main'])

    global imgWeather

    if c > 10 and (weather == "Haze" or weather == "Clear"):
        Frame(w, width=800, height=350, bg="#f78954").place(x=0, y=50)
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/sunny1.PNG"))
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
        bcolor = "#f78954"
        fcolor = "white"

    elif c > 10 and weather == "Clouds":
        Frame(w, width=800, height=350, bg="#7492b3").place(x=0, y=50)
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/cloudy1.PNG"))
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
        bcolor = "#7492b3"
        fcolor = "white"

    elif c <= 10 and weather == "Clouds":
        Frame(w, width=800, height=350, bg="#7492b3").place(x=0, y=50)
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/cloudcold.PNG"))
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
        bcolor = "#7492b3"
        fcolor = "white"

    elif c > 10 and weather == "Rain":
        Frame(w, width=800, height=350, bg="#60789e").place(x=0, y=50)
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/rain1.PNG"))
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
        bcolor = "#60789e"
        fcolor = "white"

    elif c <= 10 and (weather == "Fog" or weather == "Clear"):
        Frame(w, width=800, height=350, bg="white").place(x=0, y=50)
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/cold.PNG"))
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
        bcolor = "white"
        fcolor = "black"

    else:
        Frame(w, width=800, height=350, bg="white").place(x=0, y=50)
        Label(w, text=weather, border=0, bg='white').place(x=160, y=130)
        bcolor = "white"
        fcolor = "black"

    h = "Humidity: {}".format(result['main']['humidity'])
    p = "Pressure: {}".format(result['main']['pressure'])
    tempMax = "MAX Temp: {}".format(result['main']['temp_max'])
    tempMin = "MIN Temp: {}".format(result['main']['temp_min'])
    wSpeed = "Wind Speed: {} m/s".format(result['wind']['speed'])

    l2 = Label(w, text=month + " " + date, bg=bcolor, fg=fcolor)
    l2.config(font=("Calibry", 25))
    l2.place(x=330, y=335)

    l3 = Label(w, text=h + "%", bg=bcolor, fg=fcolor)
    l3.config(font=("Calibry", 12))
    l3.place(x=510, y=95)

    l3 = Label(w, text=p + "hPa", bg=bcolor, fg=fcolor)
    l3.config(font=("Calibry", 12))
    l3.place(x=510, y=135)

    l3 = Label(w, text=tempMin + "°C", bg=bcolor, fg=fcolor)
    l3.config(font=("Calibry", 12))
    l3.place(x=510, y=175)

    l3 = Label(w, text=tempMax + "°C", bg=bcolor, fg=fcolor)
    l3.config(font=("Calibry", 12))
    l3.place(x=510, y=215)

    l3 = Label(w, text=wSpeed, bg=bcolor, fg=fcolor)
    l3.config(font=("Calibry", 12))
    l3.place(x=510, y=255)

    l3 = Label(w, text=str(c) + "°C", bg=bcolor, fg=fcolor)
    l3.config(font=("Calibry", 42))
    l3.place(x=330, y=150)

label(a="Los Angeles")

def cmd1():
    b = str(el.get())
    label(str(b))

Button(w, image=imgSearch, command=cmd1, border=0).place(x=750, y=10)

try:
    # Try block for initial loading
    label(a="Los Angeles")
except Exception as e:
    Frame(w, width=800, height=400, bg='white').place(x=0, y=0)
    global imgNoInternet
    imgNoInternet = ImageTk.PhotoImage(Image.open("/Users/xander/Desktop/Menu/Weather_App/nointernet.PNG"))
    Label(w, image=imgNoInternet, border=0).pack(expand=True)

w.mainloop()