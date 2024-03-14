from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('', home.views.home, name='index'),
    path('menu/', home.views.menu, name='menu'),
    path('about/', home.views.about, name='about'),
    path('bookTable/', home.views.book_table, name='table')
]