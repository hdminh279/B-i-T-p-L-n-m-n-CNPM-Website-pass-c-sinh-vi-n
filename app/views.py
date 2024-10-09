from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/home.html',context)
def adminhome(request):
    context = {}
    return render(request, 'app/adminhome.html', context)
def cart(request):
    context = {}
    return render(request, 'app/cart.html', context)
def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)
def upload(request):
    context = {}
    return render(request, 'app/upload.html', context)
def login(request):
    context = {}
    return render(request, 'app/login.html', context)
def registration(request):
    context = {}
    return render(request, 'app/registration.html', context)