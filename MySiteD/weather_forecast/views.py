from django.shortcuts import render
import requests
from .forms import CityForm  
# Create your views here.


def weather_forecast(request):
    city = "Москва"
    form = CityForm(request.GET)
    if form.is_valid():
        city=form.data["name"]

    appid = '3fb5d3aebe95b7a20e70449ab17360c2'
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={appid}"

    res = requests.get(url.format(city)).json()
    lat = res[1]['lat']
    lon = res[1]['lon']
    url1 = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={appid}"

    res2 = requests.get(url1).json()
    # pprint(res2)

    print(res2['list'][0]['dt_txt'])
    count = len(res2['list'])

    
    days=list()
    for item_id in range(0, count):

        day = {'data': res2['list'][item_id]['dt_txt'],
               'temp': res2['list'][item_id]["main"]['temp'],
               'icon': res2['list'][0]['weather'][0]["icon"],
               }
        days.append(day)
    context = {'info': days, 'form':form}
    return render(request, "weather_forecast/weather_forecast.html", context)
