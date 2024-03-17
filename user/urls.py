from django.urls import path
import user.views

urlpatterns = [
    path('', user.views.user_redirect, name='user_redirect'),
    path('user_profile/', user.views.user_profile, name='user_profile'),
    path('login/', user.views.user_login, name='user_login'),
    path('register/', user.views.user_register, name='user_register')
]
