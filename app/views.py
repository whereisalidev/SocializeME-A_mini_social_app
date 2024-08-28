from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse
from django.db import IntegrityError
from .models import *



def index(request):
     return render(request, "index.html", {
        "posts": [],
        "suggestions": [],
        "page": "all_posts",
        'profile': False
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username:', username, 'pass:', password)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user) 
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'message': 'Invalid username and/or password.'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        profile = request.FILES.get('profile', None)
        cover = request.FILES.get('cover', None)

        #checking if password & confirm password don't matched?
        if password != confirmation:
            return render(request, 'register.html', {'message': "Passwords don't match!"})

        #Attempting to create User:
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.profile_pic = profile
            user.cover_pic = cover
            user.save()
        except IntegrityError:
            return render(request, "register.html", {"message": "Username already taken!"})
        
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))


    else:
        return render(request, 'register.html')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
