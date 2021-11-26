from django.urls import path
from .views import *


urlpatterns = [

    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('sing_up/', sing_up, name='sing_up'),
    path('logout/', logOut, name='logout'),
    path('add-blog/', add_blog, name='add_blog'),
    path('delete-blog/', delete_blog, name='delete_blog'),
    path('edit-blog/', edit_blog, name='edit_blog'),
    path('setting/', setting, name='setting'),


]
