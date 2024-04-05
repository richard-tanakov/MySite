from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('git', views.git,name='git'),
    path('news/', include ('news.urls'), name='news'),
    path('weather_forecast', include('weather_forecast.urls'), name='weather_forecast'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)