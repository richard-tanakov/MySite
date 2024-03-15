from django.shortcuts import render


def index(request):
    
    return render(request,'main/index.html',{'title': "Главная страница"})

def git (request):
    return render(request,'main/github.html',{'title':"Ссылки на github репозитории"})


