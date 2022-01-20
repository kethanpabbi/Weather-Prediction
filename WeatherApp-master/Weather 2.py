# importing modules

import requests
from tkinter import Tk,Label,Button,mainloop,Entry,StringVar
from PIL import ImageTk,Image

# Required Details
root = Tk()
root.geometry("320x320")
root.title("Weather App")
root.configure(bg='white')

# for images

img = ImageTk.PhotoImage(Image.open('um.png'))
panel = Label(root,image=img)
panel.place(x=112,y=3)

lable_0 = Label(root,text="Weather App",width = 20,bg='white',font=("bold",20),fg='brown')
lable_0.place(x=20,y=93)

city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names)
city_names.set("Enter City Here ...")
entry_1.place(x=70,y=140)



lable_2 = Label(root,text="Temprature : ",width = 20,bg='white',font=("bold",10),fg='blue')
lable_2.place(x=62,y=220)

lable_3 = Label(root,text="Pressure : ",width = 20,bg='white',font=("bold",10),fg='blue')
lable_3.place(x=62,y=240)

lable_5 = Label(root,text="Description : ",width = 20,bg='white',font=("bold",10),fg='blue')
lable_5.place(x=62,y=260)

lable_temp = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_temp.place(x=192,y=220)

lable_pres = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_pres.place(x=192,y=240)

lable_desc = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_desc.place(x=192,y=260)



# api config
def getTemp():

    api_key = "173285ad96bc06bf3ab830ca885d6f76"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_1.get()
    complete_url = base_url+"appid="+api_key+"&q="+city_name

# module response get

    response = requests.get(complete_url)
    x=response.json()

    if["cod"] !='404':
        y = x["main"]
        current_temprature = y["temp"]
        current_pressure = y["pressure"]

        z = x["weather"]
        weather_description = z[0]["description"]

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temprature)
        lable_desc.configure(text=weather_description)
    else:
        lable_pres.configure(text="Err")
        lable_temp.configure(text="Err")
        lable_desc.configure(text="Err")

Button(root,text="Submit",width=10,bg='brown',fg='blue',command=getTemp).place(x=122,y=170)

lable_unit = Label(root,text="Temprature in Kelvin And Pressure in mb",width = 35,bg='white',font=("bold",10),fg='brown')
lable_unit.place(x=22,y=290)

mainloop()
import urllib.request
import json
from sklearn.neighbors import KNeighborsClassifier

weather_data = []
weather_labels = []

# Write your API key here.
api_key = "173285ad96bc06bf3ab830ca885d6f76"


def get_weather_data(lat, lon):

    weather_api = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/find?lat="+lat+"&lon="+lon+"&cnt=10&appid="+api_key).read()
    weather_file = json.loads(weather_api)

    for weather_data_point in weather_file["list"]:
        temp = weather_data_point["main"]["temp"]
        pressure = weather_data_point["main"]["pressure"]
        humidity = weather_data_point["main"]["humidity"]
        wind_speed = weather_data_point["wind"]["speed"]
        wind_deg = weather_data_point["wind"]["deg"]
        clouds = weather_data_point["clouds"]["all"]
        weather_type = weather_data_point["weather"][0]["main"]

        weather_data.append([temp, pressure, humidity, wind_speed, wind_deg, clouds])
        weather_labels.append(weather_type)


def predict_weather(city_name, classifier):
    weather_api = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key).read()
    weather = json.loads(weather_api)

    temp = weather["main"]["temp"]
    pressure = weather["main"]["pressure"]
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]
    wind_deg = weather["wind"]["deg"]
    clouds = weather["clouds"]["all"]
    weather_name = weather["weather"][0]["main"]

    this_weather = [temp, pressure, humidity, wind_speed, wind_deg, clouds]
    return {"Prediction: " : classifier.predict([this_weather])[0], "Actual: " : weather_name}


# Get data from various cities
get_weather_data("50.5", "0.2")
get_weather_data("56", "3")
get_weather_data("43", "5")
for i in range(10):
    get_weather_data("46", str(i*5))

# Setup the KNeighborsClassifier
AI_machine = KNeighborsClassifier(n_neighbors=5)
AI_machine.fit(weather_data, weather_labels)

# Print predictions for a given city along with a set of the different labels in the data set.
# This allows to verify, if the prediction is incorrect, weather it is due to an inaccurate
# prediction or the actual label missing in the classifier.
print(list(set(weather_labels)))
print(predict_weather("Brussels", AI_machine))