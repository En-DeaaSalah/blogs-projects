from django.urls import path
from .views import *


urlpatterns = [

    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('sing_up/', sing_up, name='sing_up'),
    path('logout/', logOut, name='logout'),


]
