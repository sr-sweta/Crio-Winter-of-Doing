#Use aipython utube vedio  referance (In 5 steps |Using weather api in python to get weather-report of any place)
import requests
import os
from datetime import datetime

#user_id = os.environ['current_weather_data']
#environ stores the id which u need to learn to make using python

user_id = "7ee42fbaaebd27021ed55a3bafd17498"

location = input("Enter the city name: ")
#posted from website :   api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_id

api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

if api_data['cod'] == '404':
   print ("Invalid city: {}, Please check your city name".format(location))
else:
    #create variables to store and display data

    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-----x------x------x------x------x------x------x------x------x------x-----")
    print("weather states for - {} || {}".format(location.upper(),date_time))
    print("------x------x-------x------x------x------x------x-------x------x------x------")
    print("Current temp is: {:.2f} deg C".format(temp_city))
    print("Current humidity     :",hmdt)
    print("Current weather desc :",weather_desc)
    print("Current time         :",date_time)