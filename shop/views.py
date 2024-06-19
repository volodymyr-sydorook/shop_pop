from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product


@login_required(login_url='/login/')
def index(request):
    return render(request, 'shop/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'shop/login.html', {'error': 'Невірний логін або пароль'})
    return render(request, 'shop/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        else:
            return render(request, 'shop/register.html', {'error': 'Користувач з таким логіном вже існує'})
    return render(request, 'shop/register.html')


@login_required(login_url='/login/')
def cart_view(request):
    return render(request, 'shop/cart.html')


@login_required(login_url='/login/')
def catalog_view(request):
    return render(request, 'shop/catalog.html')


@login_required(login_url='/login/')
def womens_dresses_view(request):
    products = Product.objects.filter(category='Жіночі сукні')
    return render(request, 'shop/womens_dresses.html', {'products': products})


@login_required(login_url='/login/')
def womens_embroidery_view(request):
    products = Product.objects.filter(category='Жіночі вишиванки')
    return render(request, 'shop/womens_embroidery.html', {'products': products})


@login_required(login_url='/login/')
def childrens_dresses_view(request):
    products = Product.objects.filter(category='Дитячі сукні')
    return render(request, 'shop/childrens_dresses.html', {'products': products})


@login_required(login_url='/login/')
def childrens_embroidery_view(request):
    products = Product.objects.filter(category='Дитячі вишиванки')
    return render(request, 'shop/childrens_embroidery.html', {'products': products})
