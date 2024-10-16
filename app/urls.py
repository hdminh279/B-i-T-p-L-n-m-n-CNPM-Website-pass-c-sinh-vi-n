from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('adminhome/', views.adminhome, name="adminhome/"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('upload/', views.upload, name="upload"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('history/', views.history, name="history"),
    path('watch/', views.watch, name="watch"),
]
