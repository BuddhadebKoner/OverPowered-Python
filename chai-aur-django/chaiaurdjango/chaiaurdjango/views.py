from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

def home(request):
    context = {
        'current_time': timezone.now().time(),
        'current_date': timezone.now().date(),
        'current_datetime': timezone.now(),
        'current_timezone': timezone.get_current_timezone(),
    }
    return render(request, 'website/index.html', context)

def about(request):
    return HttpResponse("This is the about page of Chaiaur Django. Here you can learn more about our project and its goals.")

def contact(request):
    return HttpResponse("This is the contact page of Chaiaur Django. You can reach us at")