#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:53:08 2020

@author: kethanpabbi
"""

from urllib.request import urlopen

import json
import re
import datetime
import urllib.request
import requests

# Get Public IP


def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print Extracted Details
print( "Your City : " + city)
print( "Your Region : " + region)
print( "Your Country : " + country)
print( "Your Location : " + location)



def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '173285ad96bc06bf3ab830ca885d6f76'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')


if __name__ == '__main__':
    try:
        data_output(data_organizer(data_fetch(url_builder(1269750))))
    except IOError:
        print('no internet')
        
print('Do you want to enter a city?y/n')
a=input('Enter option:')
if a=='y':
    api_key = "173285ad96bc06bf3ab830ca885d6f76"
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name 
    city_name = input("Enter city name : ") 
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url)   
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"]  
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
        # print following values 
        print("Temperature(in kelvin unit) = " +
                    str(current_temperature) + 
          "\natmospheric pressure(in hPa unit) = " +
                    str(current_pressure) +
          "\nhumidity(in percentage) = " +
                    str(current_humidiy) +
          "\ndescription = " +
                    str(weather_description)) 
        print('Thank you!')
  
else: 
    print(" Thank you! ") 


