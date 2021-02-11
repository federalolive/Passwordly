from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stores/', views.stores_index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password/', views.generate_password, name='password'),
]