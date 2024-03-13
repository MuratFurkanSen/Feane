from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def home(request):
    page = 'Home'
    context = {'page': page}
    return render(request, 'home.html', context)


def about(request):
    page = 'About'
    context = {'page': page}
    return render(request, 'about.html', context)
