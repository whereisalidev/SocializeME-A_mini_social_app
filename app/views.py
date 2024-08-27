from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return HttpResponse('Working Fine till now...!')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')