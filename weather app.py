from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.geometry("900x500+300+200")
root.title("Weather App")
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = 'afdc7181a9e501d51c3a10c3482434c3'

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(city)
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            if result:
                home = pytz.timezone(result)
                local_time = datetime.now(home)
                current_time = local_time.strftime("%I:%M %p")
                clock.config(text=current_time)
                name.config(text="CURRENT WEATHER")

                # Weather
                lat, lon = location.latitude, location.longitude
                api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=afdc7181a9e501d51c3a10c3482434c3&units=metric"

                response = requests.get(api)
                json_data = response.json()

                if json_data.get('cod') == 200:
                    condition = json_data['weather'][0]['main']
                    description = json_data['weather'][0]['description']
                    temp = int(json_data['main']['temp'])
                    pressure = json_data['main']['pressure']
                    humidity = json_data['main']['humidity']
                    wind = json_data['wind']['speed']

                    t.config(text=f"{temp}°C")
                    c.config(text=f"{condition} | FEELS LIKE {temp}°C")
                    w.config(text=f"{wind} m/s")
                    h.config(text=f"{humidity}%")
                    d.config(text=description)
                    p.config(text=f"{pressure} hPa")
                else:
                    messagebox.showerror("Error", f"Weather data not found: {json_data.get('message')}")
            else:
                messagebox.showerror("Error", "Timezone not found.")
        else:
            messagebox.showerror("Error", "City not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Search box
search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)

# Search icon

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file="Copy of logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="Copy of box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=240, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=440, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=655, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=250, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=460, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=660, y=430)

root.mainloop()
