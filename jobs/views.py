from django.shortcuts import render

# Create your views here.


def JobsView(request):
    return render(request, 'jobs/home.html')
