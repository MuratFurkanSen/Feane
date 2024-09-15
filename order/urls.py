from django.contrib import admin
from django.urls import path, include
import order.views

urlpatterns = [
    path('', order.views.cart, name='cart')
]