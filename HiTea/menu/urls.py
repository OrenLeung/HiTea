from django.contrib import admin
from django.urls import path
from . import views as menu_views

urlpatterns = [
    path('', menu_views.getMenuData, name='menu-search'),
<<<<<<< HEAD
    path('', menu_views.getMenuData, name='menu-home'),
=======
>>>>>>> menu
]