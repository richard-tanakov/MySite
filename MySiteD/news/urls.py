from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='new_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdate.as_view(), name='news-update'),
]
