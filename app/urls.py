from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('n/login', views.login_view, name='login'),
    path('n/register', views.register, name='register')
]
