from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from item.models import Item, Category


# Create your views here.
def home(request):
    foods = Item.objects.all()
    categories = Category.objects.all()
    page = 'Home'
    context = {'page': page,
               'foods': foods,
               'categories': categories}
    return render(request, 'home.html', context)


def about(request):
    page = 'About'
    context = {'page': page}
    return render(request, 'about.html', context)


def book_table(request):
    page = 'Book Table'
    context = {'page': page}
    return render(request, 'bookTable.html', context)


def menu(request):
    page = 'Menu'
    context = {'page': page}
    return render(request, 'menu.html', context)
