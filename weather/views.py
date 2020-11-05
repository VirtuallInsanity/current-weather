from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from .forms import CityForm

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
units = 'metric'
apikey = 'c2b1732ec68315900fc6554279a8c30d'


def make_request(city):
    params = {
        'q': city,
        'units': units,
        'appid': apikey,
    }
    response = requests.get(BASE_URL, params=params).json()
    print(response)
    if response['cod'] == '404':
        return 0
    weather = {
        'city': response['name'],
        'temp': response['main']['temp'],
        'icon': response['weather'][0]['icon'],
        'description': response['weather'][0]['description']
    }
    return weather


def index(request):
    if request.method == 'POST':
        form = CityForm()
        city = request.POST['city']
        content = make_request(city)
        if content == 0:
            messages.warning(request, 'City not found!')
            content = make_request('Самара')
            render(request, 'index.html', {'form': form, 'weather': content})
        return render(request, 'index.html', {'form': form, 'weather': content})
    else:
        form = CityForm()
        content = make_request('Самара')
        return render(request, 'index.html', {'form': form, 'weather': content})
