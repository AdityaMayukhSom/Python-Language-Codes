from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'name': 'Aditya Mayukh Som'}
    return render(request, './books/profile.html', context)
