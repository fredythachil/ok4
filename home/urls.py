from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('profile/',views.profile),
    path('contact/',views.contact),
    path('register/',views.register),
    path('home/book',views.book),
]