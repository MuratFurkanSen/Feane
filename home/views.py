from django.http import HttpResponseRedirect
from django.shortcuts import render
from item.models import Item, Category
from home.models import Reservation
from home.forms import RegistrationForm


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

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = Reservation()
            data.name = form.cleaned_data['full_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.person_Count = form.cleaned_data['person_Count']
            data.date = form.cleaned_data['date']
            data.save()
            return HttpResponseRedirect('/bookTable')
    form = RegistrationForm()
    page = 'Book Table'
    context = {'page': page,
               'form': form}
    return render(request, 'bookTable.html', context)


def menu(request):

    if request.method == 'POST':
        foods = Item.objects.filter(title__icontains=request.POST['Search'])
    else:
        foods = Item.objects.all()
    categories = Category.objects.all()
    page = 'Menu'
    context = {'page': page,
               'foods': foods,
               'categories': categories}
    return render(request, 'menu.html', context)
