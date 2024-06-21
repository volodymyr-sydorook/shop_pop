from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Cart, CartProduct

def index(request):
    return render(request, 'shop/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')
        else:
            return render(request, 'shop/login.html', {'error': 'Невірний логін або пароль'})
    return render(request, 'shop/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            Cart.objects.create(user=user)  # Створюємо кошик під час реєстрації
            return redirect('login')
        else:
            return render(request, 'shop/register.html', {'error': 'Користувач з таким логіном вже існує'})
    return render(request, 'shop/register.html')

@login_required(login_url='/login/')
def catalog_view(request):
    categories = Category.objects.all()  # Отримуємо всі категорії
    return render(request, 'shop/catalog.html', {'categories': categories})

@login_required(login_url='/login/')
def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'shop/category.html', {'category': category, 'products': products})

@login_required(login_url='/login/')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)  # Перевіряємо або створюємо новий кошик
    cart_products = CartProduct.objects.filter(cart=cart)
    return render(request, 'shop/cart.html', {'cart_products': cart_products})

@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    return redirect('cart')

@login_required(login_url='/login/')
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_products = CartProduct.objects.filter(cart=cart)
    cart_products.delete()
    return render(request, 'shop/checkout.html', {'message': 'Дякуємо за покупку!'})

def custom_logout_view(request):пше
    logout(request)
    return redirect('login')
