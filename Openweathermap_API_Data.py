import json 
import requests
from pprint import pprint

# Add your API Key from https://openweathermap.org/appid

API_key = "Add_Your_Openweathermap_API_Key_Here"

# Enter the desired latitude and longitude coordinates for a weather forecast:

latitude = '41.9'
longitude = '-87.6'

# Uncomment the type of units you wish to receive forecast data in, metric or imperial:

#unit_type = 'metric'
unit_type = 'imperial'

#########################

base_url = "http://api.openweathermap.org/data/2.5/forecast?"
Final_url = base_url + "appid=" + API_key + "&lat=" + latitude + "&lon=" + longitude + "&units=" + unit_type 

forecast_json = requests.get(Final_url).json()

# Uncomment the line below to print a full response in json format from openweathermap:
#pprint(forecast_json)

#############################

# Openweathermap API json output as variables

# See https://openweathermap.org/api/hourly-forecast for explanation of data.
# openweathermap provides a forecast every three hours over the next five days.
# The forecasts are numbered from 0 to 39, you may choose which forecast time.
# Set item to the desired time period for forecast, from 0 to 39

item = 0

#############################

print()
print('Openweathermap List of data available from API in python variable format')
print('See https://openweathermap.org/api/hourly-forecast for explanation of data.')
print()

lat = forecast_json['city']['coord']['lat']
lon = forecast_json['city']['coord']['lon']
country =  forecast_json['city']['country']
id = forecast_json['city']['id']
name = forecast_json['city']['name']
population = forecast_json['city']['population']
sunrise = forecast_json['city']['sunrise']
sunset = forecast_json['city']['sunset']
timezone = forecast_json['city']['timezone']
clouds = forecast_json['list'][item]['clouds']['all']
dt = forecast_json['list'][item]['dt']
dt_txt = forecast_json['list'][item]['dt_txt']
feels_like = forecast_json['list'][item]['main']['feels_like']
grnd_level = forecast_json['list'][item]['main']['grnd_level']
humidity = forecast_json['list'][item]['main']['humidity']
pressure = forecast_json['list'][item]['main']['pressure']
sea_level = forecast_json['list'][item]['main']['sea_level']
temp = forecast_json['list'][item]['main']['temp']
temp_kf = forecast_json['list'][item]['main']['temp_kf']
temp_max = forecast_json['list'][item]['main']['temp_max']
temp_min = forecast_json['list'][item]['main']['temp_min']
pop = forecast_json['list'][item]['pop']
sys = forecast_json['list'][item]['sys']['pod']
visibility = forecast_json['list'][item]['visibility']
description = forecast_json['list'][item]['weather'][0]['description']
icon = forecast_json['list'][item]['weather'][0]['icon']
id =  forecast_json['list'][item]['weather'][0]['id']
main = forecast_json['list'][item]['weather'][0]['main']
wind_deg = forecast_json['list'][item]['wind']['deg']
wind_gust =  forecast_json['list'][item]['wind']['gust']
wind_speed =  forecast_json['list'][item]['wind']['speed']

print('lat: ' + str(lat))
print('lon: ' + str(lon))
print('country: ' + country)
print('id: ' + str(id))
print('name: ' + name)
print('population: ' + str(population))
print('sunrise: ' + str(sunrise))
print('sunset: ' + str(sunset))
print('timezone: ' + str(timezone))
print('clouds: ' + str(clouds))
print('dt: ' + str(dt))
print('dt_text: ' + dt_txt)
print('feels_like: ' + str(feels_like))
print('grnd_level: ' + str(grnd_level))
print('humidity: ' + str(humidity))
print('pressure: ' + str(pressure))
print('sea_level: ' + str(sea_level))
print('temp: ' + str(temp))
print('temp_kf: ' + str(temp_kf))
print('temp_max: ' + str(temp_max))
print('temp_min: ' + str(temp_min))
print('pop: ' + str(pop))
print('sys: ' + sys)
print('visibility: ' + str(visibility))
print('description: ' + description)
print('icon: ' + icon)
print('id: ' + str(id))
print('main: ' + main)
print('wind_deg: ' + str(wind_deg))
print('wind_gust: ' + str(wind_gust))
print('wind_speed: ' + str(wind_speed))

#########################

# Five Day Daily Forecast

# Note that the min and max temperatures apply only to the 3 hour timeframe, not the entire day.

#########################

if (unit_type == 'imperial'):
    temp_unit = ' F'
    speed_unit = ' mph'
    
if (unit_type == 'metric'):
    temp_unit = ' C'
    speed_unit = ' m/s'

print()
print('Five Day Daily Forecast')
print()

for count in range(3, 40, 8):
    print(forecast_json['list'][count]['dt_txt'])
    print(forecast_json['list'][count]['weather'][0]['description'])
    print('temp ' + str(int(forecast_json['list'][count]['main']['temp'])) + temp_unit)
    print('max ' + str(int(forecast_json['list'][count]['main']['temp_max'])) + temp_unit)
    print('min ' + str(int(forecast_json['list'][count]['main']['temp_min'])) + temp_unit)
    print('pressure ' + str(forecast_json['list'][count]['main']['pressure']) + ' mbar')
    print('wind speed ' + str(forecast_json['list'][count]['wind']['speed']) + speed_unit)
    print('wind gust ' + str(forecast_json['list'][count]['wind']['gust']) + speed_unit)
    print('wind deg ' + str(forecast_json['list'][count]['wind']['deg']) + ' deg')
    print()


      