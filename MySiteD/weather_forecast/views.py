from django.shortcuts import render
import requests
# Create your views here.


def weather_forecast(request):
    appid = '3fb5d3aebe95b7a20e70449ab17360c2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid
    city = "Moscow"
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
    }

    context = {'info': city_info}
    return render(request, "weather_forecast/weather_forecast.html", context)
