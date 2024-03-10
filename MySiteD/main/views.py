from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def cript (request):
    return render(request,'main/cont_cript.html')


