
from django.contrib import admin
from django.urls import path, include
from . import views

app_name='ecomapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('allproducts',views.allproducts,name='allproducts'),
    path('about/',views.about,name='about'),
    path('registration/',views.register,name='register'),
    path('login/',views.loginn,name='login'),
    path('logout',views.logoutt,name='logout'),
    path('products',views.products,name='product'),
    path('categories/',views.categories,name='cateories'),
    path('categorie/<str:slug>',views.categoriess,name='cat_product'),
    path('productdetails/<str:cat_slug>/<str:p_slug>',views.productdetail,name='productdetail'),
    path('search/',views.search,name='search'),
    # path('test',views.test,name='test'),


]
