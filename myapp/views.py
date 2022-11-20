from django.shortcuts import render
import requests

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=69989cbe7fc2d505184be86b3b09904a'

    city = 'Pune'

    city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather) #checking the output
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'wind' : city_weather['wind']['speed']
    }

    city1 = 'Kerala'

    city_weather1 = requests.get(url.format(city1)).json()
    print(city_weather1)

    ker_weather = {
        'city' : city1,
        'temperature' : city_weather1['main']['temp'],
        'description' : city_weather1['weather'][0]['description'],
        'icon' : city_weather1['weather'][0]['icon'],
        'wind' : city_weather1['wind']['speed']
    }

    city2 = 'Bangalore'

    city_weather2 = requests.get(url.format(city2)).json()
    print(city_weather2)

    blr_weather = {
        'city' : city2,
        'temperature' : city_weather2['main']['temp'],
        'description' : city_weather2['weather'][0]['description'],
        'icon' : city_weather2['weather'][0]['icon'],
        'wind' : city_weather2['wind']['speed']
    }

    city3 = 'Mumbai'

    city_weather3 = requests.get(url.format(city3)).json()
    print(city_weather3)

    mum_weather = {
        'city' : city3,
        'temperature' : city_weather3['main']['temp'],
        'description' : city_weather3['weather'][0]['description'],
        'icon' : city_weather3['weather'][0]['icon'],
        'wind' : city_weather3['wind']['speed']
    }

    city4 = 'Goa'

    city_weather4 = requests.get(url.format(city4)).json()
    print(city_weather4)

    ga_weather = {
        'city' : city4,
        'temperature' : city_weather4['main']['temp'],
        'description' : city_weather4['weather'][0]['description'],
        'icon' : city_weather4['weather'][0]['icon'],
        'wind' : city_weather4['wind']['speed']
    }

    city5 = 'London'

    city_weather5 = requests.get(url.format(city5)).json()
    print(city_weather5)

    lon_weather = {
        'city' : city5,
        'temperature' : city_weather5['main']['temp'],
        'description' : city_weather5['weather'][0]['description'],
        'icon' : city_weather5['weather'][0]['icon'],
        'wind' : city_weather5['wind']['speed']
    }

    city6 = 'Chicago'

    city_weather6 = requests.get(url.format(city6)).json()
    print(city_weather6)

    chi_weather = {
        'city' : city6,
        'temperature' : city_weather6['main']['temp'],
        'description' : city_weather6['weather'][0]['description'],
        'icon' : city_weather6['weather'][0]['icon'],
        'wind' : city_weather6['wind']['speed']
    }



    return render(request, 'index.html', {'weather' : weather, 'ker_Weather' : ker_weather, 'blr_Weather' : blr_weather, 'mum_Weather' : mum_weather, 'ga_Weather' : ga_weather, 'lon_Weather' : lon_weather, 'chi_Weather' : chi_weather}) #returns the index.html template