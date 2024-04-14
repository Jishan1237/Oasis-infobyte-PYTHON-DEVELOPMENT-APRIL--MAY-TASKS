import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from datetime import datetime

def getweather(city):
    try:
        apikey = '6b556005dae9d19ffd7918ac69d92c9f'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return None

def updateweather():
    city = cityentry.get()
    if city:
        weatherdata = getweather(city)
        if weatherdata:
            iconurl = f"http://openweathermap.org/img/w/{weatherdata['weather'][0]['icon']}.png"
            temperature = weatherdata['main']['temp']
            description = weatherdata['weather'][0]['description']
            image = Image.open(requests.get(iconurl, stream=True).raw)
            photo = ImageTk.PhotoImage(image)
            weathericon.config(image=photo)
            weathericon.image = photo
            weatherinfo.config(text=description, font=("Arial", 16), background='#79CBCA', foreground='white')
            tempLabel.config(text=f"Temperature: {temperature}°C", font=("Arial", 16), background='#79CBCA', foreground='white')
        else:
            weatherinfo.config(text="City not found", font=("Arial", 16), background='#79CBCA', foreground='white')
    else:
        weatherinfo.config(text="Please enter a city", font=("Arial", 16), background='#79CBCA', foreground='white')

def updatetime():
    now = datetime.now()
    timeStr = now.strftime("%I:%M:%S %p")
    timelabel.config(text=f"Current time: {timeStr}", font=("Arial", 14), background='#77A1D3', foreground='white')
    root.after(1000, updatetime)

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(background='#77A1D3')

style = ttk.Style()
style.configure('TButton', font=('Arial', 14))

citylabel = ttk.Label(root, text="Enter city name:", font=("Arial", 16), background='#77A1D3', foreground='white')
citylabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

cityentry = ttk.Entry(root, font=("Arial", 16))
cityentry.grid(row=0, column=1, padx=10, pady=5)

getweatherbutton = ttk.Button(root, text="Get Weather", command=updateweather, style='TButton')
getweatherbutton.grid(row=0, column=2, padx=10, pady=5, sticky="w")  

weatherinfo = ttk.Label(root, text="", font=("Arial", 16), background='#79CBCA', foreground='white')
weatherinfo.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

weathericon = ttk.Label(root, background='#79CBCA')
weathericon.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

tempLabel = ttk.Label(root, text="", font=("Arial", 16), background='#79CBCA', foreground='white')
tempLabel.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

timelabel = ttk.Label(root, text="", font=("Arial", 14), background='#77A1D3', foreground='white')
timelabel.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

updatetime()
root.mainloop()
