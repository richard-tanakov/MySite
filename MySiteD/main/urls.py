from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('cript', views.cript,name='cript'),
    path('news/', include ('news.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)