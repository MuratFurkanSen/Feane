from django.contrib.auth import login, authenticate

from user.forms import UserRegisterForm, UserLoginForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from user.models import UserProfile


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            authenticate(username=username, password=password)
            return HttpResponseRedirect('/user/user_profile/')

    form = UserRegisterForm()
    page = 'Register'
    context = {'page': page,
               'form': form}
    return render(request, 'user_section.html', context)


def user_login(request):
    if request.method == 'POST':
        print("Hallo")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print("Welcome " + username)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/user_profile')
            else:
                return HttpResponseRedirect('/user/login')

    form = UserLoginForm()
    page = 'Login'
    context = {'page': page,
               'form': form}
    return render(request, 'user_section.html', context)



def user_profile(request):
    if request.user.is_authenticated:
        pass


def user_redirect(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user/user_profile/')
    else:
        return HttpResponseRedirect('/user/login/')
