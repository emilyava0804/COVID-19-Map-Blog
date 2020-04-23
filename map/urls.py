from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as map_views

urlpatterns = [
   path('about/', map_views.about, name='about'),
   path('home/', map_views.home, name='home'),
   path('map/', map_views.map, name='map'),
   path('information/', map_views.information, name='information'),
   path('blog/', map_views.blog, name='blog'),
   path('profile/', map_views.profile, name='profile')

]