from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('', home.views.home, name='index'),
    path('about/', home.views.about, name='about')
]