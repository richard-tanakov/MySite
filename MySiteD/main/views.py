from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def uniswap (request):
    return render(request,'main/cont_uniswap.html')


