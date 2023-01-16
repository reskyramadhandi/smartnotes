from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'forms/home.html')


def order(request):
    return render(request, 'forms/order.html')
